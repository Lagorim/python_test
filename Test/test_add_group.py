# -*- coding: utf-8 -*-
from Model_class.group import Group


def test_add_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="fhgfhg", header="jdhajhddh", footer="dakjdkjad"))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="", header="", footer=""))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)


def test_add_igor_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="Igor", header="Pronin", footer=""))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)


def test_add_nikas_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="Nikas", header="Proninas", footer="Anatoly"))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)


def test_add_nika_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="Nika", header="Proninas", footer="Anatoly"))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)


def test_add_nika_s_group(app):
     old_groups = app.group.get_group_list()
     app.group.create(Group(name="Nika", header="Pronina", footer="Anatoly"))
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)
