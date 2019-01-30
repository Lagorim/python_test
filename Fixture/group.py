
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def click_content(self):
        wd = self.app.wd
        wd.find_element_by_id("content").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def submit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def selected_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_group(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def form_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.click_content()
        self.open_groups_page()
        # init group creation
        self.new_group()
        # fill group form
        self.form_group(group)
        self.submit_group()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.click_content()
        self.open_groups_page()
        #select first group
        self.selected_group()
        #submit delete group
        self.delete_group()
        self.return_to_groups_page()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        self.selected_group()
        #edit group
        self.edit_group()
        self.form_group(group)
        self.update_group()
        self.return_to_groups_page()





