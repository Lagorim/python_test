# -*- coding: utf-8 -
import pytest
from Model_class.contact import Contact
from Fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminated)
    return fixture


def test_add_igor_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Igor", lastname=
        "Pronin"))
        app.logout()

def test_add_andrey_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Andrey", lastname=
        "Ivanov"))
        app.logout()

def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", lastname=
        ""))
        app.logout()

def test_add_nika_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Nika", lastname=
        "Pronina"))
        app.logout()

def test_add_igor_rus_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Игорь", lastname=
        "Пронин"))
        app.logout()

def test_add_nika_rus_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="ника", lastname=
        "пронина"))
        app.logout()

