from model.group import Group
from model.contact import Contact

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new_group_name"))
    app.session.logout()


def test_modify_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))
    app.session.logout()