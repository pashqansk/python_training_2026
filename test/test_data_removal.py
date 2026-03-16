from model.contact import Contact
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # из списка групп вырезаем 1 группу
    old_groups [0:1] = []
    # сравниваем объекты списка группы
    assert old_groups == new_groups


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)