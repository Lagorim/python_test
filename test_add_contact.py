# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_igor_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Igor", lastname=
        "Pronin"))
        self.logout()

    def test_add_andrey_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Andrey", lastname=
        "Ivanov"))
        self.logout()

    def test_add_empty_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="", lastname=
        ""))
        self.logout()

    def test_add_nika_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Nika", lastname=
        "Pronina"))
        self.logout()

    def test_add_igor_rus_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Игорь", lastname=
        "Пронин"))
        self.logout()

    def test_add_nika_rus_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="ника", lastname=
        "пронина"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contact_page()
        # create contact
        wd.find_element_by_name("firstname").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
