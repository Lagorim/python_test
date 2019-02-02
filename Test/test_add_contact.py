# -*- coding: utf-8 -
from Model_class.contact import Contact


def test_add_igor_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Igor", lastname="Pronin"))
        app.session.logout()

def test_add_andrey_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Andrey", lastname="Ivanov"))
        app.session.logout()

def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="", lastname=""))
        app.session.logout()

def test_add_nika_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Nika", lastname="Pronina"))
        app.session.logout()

def test_add_igor_rus_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Игорь", lastname="Пронин"))
        app.session.logout()

def test_add_nika_rus_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="ника", lastname="пронина"))
        app.session.logout()

