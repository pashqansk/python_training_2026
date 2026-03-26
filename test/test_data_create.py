from string import punctuation

from model.group import Group
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# DDT Вариант полного перебора полей
'''group_testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("N***", 10)]
    for header in ["", random_string("H***", 20)]
    for footer in ["", random_string("F***", 20)]]'''

# DDT Окончательный вариант
group_testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("N***", 10),
          header=random_string("H***", 20),
          footer=random_string("F***", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", group_testdata, ids=[repr(x) for x in group_testdata])
def test_add_group(app, group):
        old_groups = app.group.get_group_list()
        app.group.create_group(group)
        # проверяем что новая группа добавлена. сверяется длина старого списка с общим количеством групп
        # count() выступает в качестве хэша
        assert len(old_groups) + 1 == app.group.count()
        # загружаем список групп
        new_groups = app.group.get_group_list()
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


contact_testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("FN", 10),
            midname=random_string("MN", 10),
            lastname=random_string("LN", 10),
            nickname=random_string("NN", 10),
            title=random_string("TI", 20),
            workname=random_string("WORK", 10),
            homeaddr=random_string("ADDR", 20),
            homephone=random_string("HPh", 5),
            mobilephone=random_string("MPh", 10),
            workphone=random_string("WPh", 15),
            email1=random_string("E1", 5),
            email2=random_string("E2", 10),
            email3=random_string("E3", 15),
            url=random_string("URL", 20),
            bday="1",
            bmonth="January",
            byear="1995",
            aday="1",
            amonth="January",
            ayear="2025"
            )
    for n in range(5)
]

@pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create_contact(contact)
        # сюда тоже сверку с хэшем можно прикрутить, т.к. метод уже существует
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        # добавляем ту же группу в список old_groups
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)