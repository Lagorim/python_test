from Model_class.group import Group


def test_modify_group_name_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FOtterY"))
    app.group.modify_first_group(Group(name=""))


def test_modify_group_name_ru(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    app.group.modify_first_group(Group(name="ЫВПРЫф"))


def test_modify_group_name_rus(app):
    if app.group.count() == 0:
        app.group.create(Group(name="ЫФПАРЫО"))
    app.group.modify_first_group(Group(name=""))


def test_modify_group_name_number(app):
    if app.group.count() == 0:
        app.group.create(Group(name="12451!"))
    app.group.modify_first_group(Group(name=""))


def test_modify_group_name_numbers(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    app.group.modify_first_group(Group(name="123446:!"))


def test_modify_group_header_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(header=""))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="HJHDJS"))
    app.group.modify_first_group(Group(header=""))


def test_modify_group_header_ru(app):
    if app.group.count() == 0:
        app.group.create(Group(header=""))
    app.group.modify_first_group(Group(header="ЫВПРЫф"))


def test_modify_group_header_rus(app):
    if app.group.count() == 0:
        app.group.create(Group(header="ЫФПАРЫО"))
    app.group.modify_first_group(Group(header=""))


def test_modify_group_header_number(app):
    if app.group.count() == 0:
        app.group.create(Group(header="12451!"))
    app.group.modify_first_group(Group(header=""))


def test_modify_group_header_numbers(app):
    if app.group.count() == 0:
        app.group.create(Group(header=""))
    app.group.modify_first_group(Group(header="123446:!"))


def test_modify_group_footer_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(footer=""))
    app.group.modify_first_group(Group(footer="New footer"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="kJHSJ"))
    app.group.modify_first_group(Group(footer=""))


def test_modify_group_footer_ru(app):
    if app.group.count() == 0:
        app.group.create(Group(footer=""))
    app.group.modify_first_group(Group(footer="ЫВПРЫф"))


def test_modify_group_footer_rus(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="ЫФПАРЫО"))
    app.group.modify_first_group(Group(footer=""))


def test_modify_group_footer_number(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="12451!"))
    app.group.modify_first_group(Group(footer=""))


def test_modify_group_footer_numbers(app):
    if app.group.count() == 0:
        app.group.create(Group(footer=""))
    app.group.modify_first_group(Group(footer="123446:!"))