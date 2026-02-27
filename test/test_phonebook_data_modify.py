from model.group import Group
from model.contact import Contact

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group_name(Group(name="new_group_name"))
    app.session.logout()


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact_name(Contact(firstname="new_contact_name"))
    app.session.logout()