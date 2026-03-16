from model.group import Group
from model.contact import Contact


def test_add_group(app):
        old_groups = app.group.get_group_list()
        app.group.create_group(Group(name="1345134534531t", header="qaegheryearhaerheasrseh", footer="asdhrehsdfhdhdrh"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
        old_groups = app.group.get_group_list()
        app.group.create_group(Group())
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)


def test_add_contact(app):
        app.contact.create_contact(Contact(
            firstname="Vasya",
            midname="Andreevich",
            lastname="Pupkin",
            nickname="Kosoi",
            title="che tyt nado pisat",
            workname="kgb",
            homeaddr="Pushkina, 42",
            cityphone="2174545",
            mobilephone="79991112345",
            workphone="88005553535",
            email1="qwe@rty.io",
            email2="asd@fgh.jk",
            email3="zxc@vbn.mu",
            url="https://ya.ru",
            bday="1",
            bmonth="January",
            byear="1995",
            aday="1",
            amonth="January",
            ayear="2025"))