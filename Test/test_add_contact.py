# -*- coding: utf-8 -
from Model_class.contact import Contact


def test_add_igor_contact(app):
    app.contact.create(Contact(firstname="Igor", lastname="Pronin"))


def test_add_andrey_contact(app):
    app.contact.create(Contact(firstname="Andrey", lastname="Ivanov"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname=""))


def test_add_nika_contact(app):
    app.contact.create(Contact(firstname="Nika", lastname="Pronina"))


def test_add_igor_rus_contact(app):
    app.contact.create(Contact(firstname="Игорь", lastname="Пронин"))


def test_add_nika_rus_contact(app):
    app.contact.create(Contact(firstname="ника", lastname="пронина"))

