from model.group import Group
from model.contact import Contact


def test_add_group(app):
        old_groups = app.group.get_group_list()
        group = Group(name="1345134534531t", header="qaegheryearhaerheasrseh", footer="asdhrehsdfhdhdrh")
        app.group.create_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
        old_groups = app.group.get_group_list()
        group = Group(name="", header="", footer="")
        app.group.create_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(
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
            ayear="2025")
        app.contact.create_contact(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        # добавляем ту же группу в список old_groups
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)