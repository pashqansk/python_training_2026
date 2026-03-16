from model.group import Group
from model.contact import Contact


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="new_group_name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new_group_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)