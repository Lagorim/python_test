from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from Fixture.session_group import SessionHelperGroup
from Fixture.session_contact import SessionHelperContact
from Fixture.group import GroupHelper
from Fixture.contact import ContactHelper

class Application():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_group = SessionHelperGroup(self)
        self.session_contact = SessionHelperContact(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def terminated(self):
        self.wd.quit()