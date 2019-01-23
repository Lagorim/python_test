# -*- coding: utf-8 -*-
from Model_class.group import Group


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
        app.group.create(Group(name="Igor", header="Pronin", footer=""))
        app.session_group.logout()

