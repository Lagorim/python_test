# -*- coding: utf-8 -*-
import pytest
from Model_class.group import Group
from Fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminated)
    return fixture


def test_add_group(app):
        app.session_group.login(username="admin", password="secret")
        app.group.create(Group(name="fhgfhg", header="jdhajhddh", footer="dakjdkjad"))
        app.session_group.logout()

def test_add_empty_group(app):
        app.session_group.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session_group.logout()

def test_add_igor_group(app):
        app.session_group.login(username="admin", password="secret")
        app.create(Group(name="Igor's", header="Pronin", footer="'''"))
        app.session_group.logout()

