from model.group import Group
from model.contact import Contact

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new_group_name", header="new_header", footer="new_footer"))
    app.session.logout()


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(
                                firstname="new_firstname",
                                midname="new_middlename",
                                lastname="new_lastname",
                                nickname="new_nickname",
                                title="new_title",
                                workname="new_workname",
                                homeaddr="new_homeaddress",
                                cityphone="new_cityphone",
                                mobilephone="new_mobilephone",
                                workphone="new_workphone",
                                email1="new_email1",
                                email2="new_email2",
                                email3="new_email3",
                                url="new_url",
                                bday="11",
                                bmonth="November",
                                byear="2000",
                                aday="11",
                                amonth="November",
                                ayear="2222"))
    app.session.logout()