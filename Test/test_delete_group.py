
def test_delete_first_group(app):
    app.session_group.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session_group.logout()