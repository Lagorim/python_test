from Model_class.group import Group


def test_edit_first_group(app):
    app.group.edit(Group(name="abckj", header="joiuh", footer="vgxsrdgc"))
