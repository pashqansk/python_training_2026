import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test-Fname", lastname="test-Lname"))
    if len(orm.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    app.contact.add_contact_to_group(contact.id, group_id)
    group_members = orm.get_contacts_in_group(Group(id=group_id))
    assert contact in group_members


def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.contact.create(Contact(firstname="test-Fname", lastname="test-Lname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        all_contacts = orm.get_contact_list()
        contact = random.choice(all_contacts)
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    contact_to_remove = random.choice(contacts_in_group)
    app.contact.remove_contact_from_group(contact_to_remove.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    assert contact_to_remove not in new_contacts