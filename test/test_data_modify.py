import random
from model.group import Group
from model.contact import Contact


def test_modify_random_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, Group(name="new_group_name"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    modified_group = Group(id=group.id, name="new_group_name")
    old_groups = [modified_group if g.id == group.id else g for g in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # сверка  DB - UI
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_random_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test-Fname",lastname="test-Lname"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, Contact(firstname="new_firstname", lastname="new_lastname"))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    modified_contact = Contact(id=contact.id, firstname="new_firstname", lastname="new_lastname")
    old_contacts = [modified_contact if c.id == contact.id else c for c in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # сверка  DB - UI
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
