# -*- coding: utf-8 -*-
from Model_class.group import Group



def test_add_group(app):
     old_groups = app.group.get_group_list()
     group = Group(name="fhgfhg", header="jdhajhddh", footer="dakjdkjad")
     app.group.create(group)
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_max ) == sorted(new_groups, key=Group.id_or_max)


#def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_igor_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="Igor", header="Pronin", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_nikas_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="Nikas", header="Proninas", footer="Anatoly")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_nika_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="Nika", header="Proninas", footer="Anatoly")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_nika_s_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="Nika", header="Pronina", footer="Anatoly")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
