from Model_class.group import Group

def test_edit_first_group(app):
        app.session_group.login(username="admin", password="secret")
        app.group.edit(Group(name="abckj", header="joiuh", footer="vgxsrdgc"))
        app.session_group.logout()