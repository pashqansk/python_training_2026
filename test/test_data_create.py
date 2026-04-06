from model.group import Group
from model.contact import Contact


def test_add_group(app, db, json_groups, check_ui):
        group = json_groups
        old_groups = db.get_group_list()
        app.group.create_group(group)
        # загружаем список групп
        new_groups = db.get_group_list()
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        # сверка  DB - UI
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_add_contact(app, db, json_contacts, check_ui):
        contact = json_contacts
        old_contacts = db.get_contact_list()
        app.contact.create_contact(contact)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        # сверка  DB - UI
        if check_ui:
                assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
