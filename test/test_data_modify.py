from random import randrange
from model.group import Group
from model.contact import Contact


def test_modify_random_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    # определяем индекс изменяемой группы случайным образом
    index = randrange(len(old_groups))
    group = Group(name="new_group_name")
    group.id = old_groups[index].id
    # передаем в качестве параметра порядковый номер изменяемой группы
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Этот тест будет удален после использования параметризованных тестов
'''def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new_group_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''


def test_modify_random_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test-Fname",lastname="test-Lname"))
    # формируем список
    old_contacts = app.contact.get_contact_list()
    # рандомно определяем порядковый номер (id) изменяемого контакта
    index = randrange(len(old_contacts))
    contact = Contact(
        firstname="new_firstname",
        lastname="new_lastname")
    contact.id = old_contacts[index].id
    # в параметре передаем порядковый номер того контакта, который изменяем
    app.contact.modify_contact_by_index(index, contact)
    # формируем новый список с учётом измененного контакта
    new_contacts = app.contact.get_contact_list()
    # сверяем количество элементов в изначальном и новом списках
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    # сверяем отсортированные списки
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)