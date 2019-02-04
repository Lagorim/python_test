from Model_class.contact import Contact


def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=""))
    app.contact.modify_first_contact(Contact(firstname="Firstname"))


def test_modify_firstname_empty_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=""))
    app.contact.modify_first_contact(Contact(firstname=""))


def test_modify_firstname_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="bhsbdjj"))
    app.contact.modify_first_contact(Contact(firstname=""))


def test_modify_firstname_ru(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=""))
    app.contact.modify_first_contact(Contact(firstname="РВИООЫВЛ"))


def test_modify_firstname_rus(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="ОРИВРЫОРП"))
    app.contact.modify_first_contact(Contact(firstname="РВИООЫВЛ"))


def test_modify_firstname_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=""))
    app.contact.modify_first_contact(Contact(firstname="1546258:`"))

def test_modify_firstname_numbers(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="12565715!:"))
    app.contact.modify_first_contact(Contact(firstname=""))


def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.modify_first_contact(Contact(lastname="Lastname"))


def test_modify_lastname_empty_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.modify_first_contact(Contact(lastname=""))


def test_modify_lastname_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="bhsbdjj"))
    app.contact.modify_first_contact(Contact(lastname=""))


def test_modify_lastname_ru(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.modify_first_contact(Contact(lastname="РВИООЫВЛ"))


def test_modify_lastname_rus(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="ОРИВРЫОРП"))
    app.contact.modify_first_contact(Contact(lastname="РВИООЫВЛ"))


def test_modify_lastname_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.modify_first_contact(Contact(lastname="1546258:`"))


def test_modify_lastname_numbers(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="12565715!:"))
    app.contact.modify_first_contact(Contact(lastname=""))
