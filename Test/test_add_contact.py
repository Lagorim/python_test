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
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Igor", lastname=
        "Pronin"))
        app.session_contact.logout()

def test_add_andrey_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Andrey", lastname=
        "Ivanov"))
        app.session_contact.logout()

def test_add_empty_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", lastname=
        ""))
        app.session_contact.logout()

def test_add_nika_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Nika", lastname=
        "Pronina"))
        app.session_contact.logout()

def test_add_igor_rus_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Игорь", lastname=
        "Пронин"))
        app.session_contact.logout()

def test_add_nika_rus_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="ника", lastname=
        "пронина"))
        app.session_contact.logout()

