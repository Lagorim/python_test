from Model_class.group import Group


def test_modify_group_name_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="FOtterY"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_name_ru(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="ЫВПРЫф"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_name_rus(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="ЫФПАРЫО"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_name_number(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="12451!"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_name_numbers(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="123446:!"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header_empty(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="HJHDJS"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header_ru(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="ЫВПРЫф"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header_rus(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="ЫФПАРЫО"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header_number(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="12451!"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header_numbers(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="123446:!"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer_empty(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="kJHSJ"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer_ru(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="ЫВПРЫф"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer_rus(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="ЫФПАРЫО"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer_number(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="12451!"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer_numbers(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer=""))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="123446:!"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)