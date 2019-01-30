from Model_class.contact import Contact

def test_add_igor_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="xxxxx", lastname="bnkjshakd"))
    app.session_contact.logout()