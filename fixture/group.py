from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        # проверяю нужный url и кнопки-ориентира: если их нет, то осуществляю переход на страницу списка групп
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_first_group(self):
            wd = self.app.wd
            wd.find_element_by_name("selected[]").click()


    def select_group_by_index(self, index):
            wd = self.app.wd
            wd.find_elements_by_name("selected[]")[index].click()


    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        # сброс кэша после совершенных с ним операций
        self.group_cache = None


    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        # сброс кэша после совершенных с ним операций
        self.group_cache = None


    def modify_first_group(self):
        self.modify_group_by_index(0, Group(name="test"))


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        # сброс кэша после совершенных с ним операций
        self.group_cache = None


    def delete_first_group(self):
        self.delete_group_by_index(0)


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len (wd.find_elements_by_name("selected[]"))


    group_cache = None


    def get_group_list(self):
        # если кэш пустой, то формируем его загружая информацию из браузера
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            # для каждого элемента входящего в "группы" находим имя и id
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                # создаем объект типа Group и добавляем его в список
                self.group_cache.append(Group(name=text, id=id))
        # в тестах работаем не с самим кэшем, а с его копией
        return list(self.group_cache)
