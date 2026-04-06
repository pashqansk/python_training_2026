import random
from model.contact import Contact
from model.group import Group

def test_delete_random_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # передаем в качестве параметра id удаляемой группы
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # из списка групп вырезаем 1 группу
    old_groups.remove(group)
    # сравниваем объекты списка группы
    assert old_groups == new_groups


def test_delete_random_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # передаем в качестве параметра id удаляемого контакта
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # вырезаем первый контакт из списка контактов
    old_contacts.remove(contact)
    # сравниваем старый список контактов с актуальным списком контактов после удаления контакта
    assert old_contacts == new_contacts