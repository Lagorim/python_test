from Model_class.contact import Contact

def test_modify_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Firstname"))
    app.session.logout()

def test_modify_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Lastname"))
    app.session.logout()