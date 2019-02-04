from Model_class.contact import Contact


def test_delete_first_contact(app):
    if app.group.count() == 0:
        app.group.create(Contact(firstname="jadjsda"))
    app.contact.delete_first_contact()
