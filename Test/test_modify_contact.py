from Model_class.contact import Contact


def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Firstname"))


def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Lastname"))
