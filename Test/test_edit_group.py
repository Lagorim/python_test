from Model_class.group import Edit

def test_edit_first_group(app):
    app.session_group.login(username="admin", password="secret")
    app.edit.group(Edit(name="cgfcc", header="joiuh", footer="vgxsrdgc"))
    app.session_group.logout()