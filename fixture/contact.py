from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def open_contacts_page(self):
        wd = self.app.wd
        # проверяю наличие кнопок-ориентиров: если их нет, то осуществляю переход на страницу списка контактов
        if not len(wd.find_elements_by_name("Sort on “Last name”")) > 0 and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.midname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.workname)
        self.change_field_value("address", contact.homeaddr)
        self.change_field_value("home", contact.cityphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.url)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)


    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[19]").click()
        self.open_contacts_page()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.open_contacts_page()



    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_contacts_page()


    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))