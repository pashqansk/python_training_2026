from model.group import Group
from model.contact import Contact


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="new_group_name"))


def test_modify_first_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))