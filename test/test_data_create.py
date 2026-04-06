from model.group import Group
from model.contact import Contact


def test_add_group(app, db, json_groups):
        group = json_groups
        old_groups = db.get_group_list()
        app.group.create_group(group)
        # загружаем список групп
        new_groups = db.get_group_list()
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_contact(app, db, json_contacts):
        contact = json_contacts
        old_contacts = db.get_contact_list()
        app.contact.create_contact(contact)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)