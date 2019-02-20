from Model_class.contact import Contact
from random import randrange

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Firstname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_firstname_empty_all(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_firstname_empty(app):
#            if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="bhsbdjj"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_firstname_ru(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="РВИООЫВЛ"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_firstname_rus(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="ОРИВРЫОРП"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="РВИООЫВЛ"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_firstname_number(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="1546258:`"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_modify_firstname_numbers(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="12565715!:"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="Lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_empty_all(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_empty(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="bhsbdjj"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_ru(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="РВИООЫВЛ"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_rus(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="ОРИВРЫОРП"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="РВИООЫВЛ"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_number(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname=""))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="1546258:`"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_lastname_numbers(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="12565715!:"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
