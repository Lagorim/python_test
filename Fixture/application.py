from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from Fixture.session_group import SessionHelperGroup
from Fixture.session_contact import SessionHelperContact

class Application():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_group = SessionHelperGroup(self)
        self.session_contact = SessionHelperContact(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def click_content(self):
        wd = self.wd
        wd.find_element_by_id("content").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.click_content()
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group()
        self.return_to_groups_page()

    def submit_group(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

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

    def terminated(self):
        self.wd.quit()