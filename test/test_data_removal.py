from random import randrange
from model.contact import Contact
from model.group import Group

def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    # определяем индекс удаляемой группы случайным образом
    index = randrange(len(old_groups))
    # передаем в качестве параметра порядковый номер удаляемой группы
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # из списка групп вырезаем 1 группу
    old_groups [index:index+1] = []
    # сравниваем объекты списка группы
    assert old_groups == new_groups


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    # определяем индекс удаляемого контакта
    index = randrange(len(old_contacts))
    # передаем в качестве параметра номер удаляемого контакта
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # вырезаем первый контакт из списка контактов
    old_contacts [index:index+1] = []
    # сравниваем старый список контактов с актуальным списком контактов после удаления контакта
    assert old_contacts == new_contacts