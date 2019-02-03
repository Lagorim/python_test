from Model_class.contact import Contact


def test_add_igor_contact(app):
    app.contact.edit(Contact(firstname="xxxxx", lastname="bnkjshakd"))
