# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact
from application import Application

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_add_igor_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Igor", lastname=
        "Pronin"))
        self.app.logout()

    def test_add_andrey_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Andrey", lastname=
        "Ivanov"))
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="", lastname=
        ""))
        self.app.logout()

    def test_add_nika_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Nika", lastname=
        "Pronina"))
        self.app.logout()

    def test_add_igor_rus_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Игорь", lastname=
        "Пронин"))
        self.app.logout()

    def test_add_nika_rus_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="ника", lastname=
        "пронина"))
        self.app.logout()

    def tearDown(self):
        self.app.terminated()

if __name__ == "__main__":
    unittest.main()
