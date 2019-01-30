
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()

    def edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def message_delete_contact(self):
        wd = self.app.wd
        wd.find_elements_by_css_selector("div.msgbox")

    def form_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # create contact
        self.form_contact(contact)
        # submit
        self.submit_contact()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        self.select_first_contact()
        #submit delete contact
        self.delete_contact()
        wd.switch_to_alert().accept()
        self.message_delete_contact()

    def edit(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # edit contact
        self.edit_contact()
        # fill contact form
        self.form_contact(contact)
        # submit
        self.update_contact()
