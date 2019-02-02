# -*- coding: utf-8 -*-
from Model_class.group import Group


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="fhgfhg", header="jdhajhddh", footer="dakjdkjad"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()

def test_add_igor_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="Igor", header="Pronin", footer=""))
        app.session.logout()

def test_add_nikas_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="Nika's", header="Pronina's", footer="Anatoly"))
        app.session.logout()

def test_add_nika_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="Nika", header="Pronina's", footer="Anatoly"))
        app.session.logout()

def test_add_nika_s_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="Nika", header="Pronina", footer="Anatoly"))
        app.session.logout()