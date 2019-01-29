

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
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

    #def return_to_home_page(self):
        #wd = self.app.wd
        #wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #submit delete contact
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")

    def edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first contact
        wd.find_element_by_id("79").click()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit
        wd.find_element_by_name("update").click()
