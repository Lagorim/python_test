# -*- coding: utf-8 -
from Model_class.contact import Contact


def test_add_igor_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Igor", lastname="Pronin"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_andrey_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Andrey", lastname="Ivanov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", lastname=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_nika_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Nika", lastname="Pronina"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_igor_rus_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Игорь", lastname="Пронин"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_nika_rus_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="ника", lastname="пронина"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

