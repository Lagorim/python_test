
class EditContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def edit(self, contact):
        wd = self.app.wd
        self.open_contact()
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