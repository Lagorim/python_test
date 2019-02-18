from Model_class.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
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
        wd = self.change_field_value("firstname", contact.firstname)
        wd = self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
        return wd

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len (wd.find_elements_by_name("selected[]"))

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

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # edit contact
        self.edit_contact()
        # fill contact form
        self.form_contact(new_contact_data)
        # submit
        self.update_contact()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            text = cells[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts
