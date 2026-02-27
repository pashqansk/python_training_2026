# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="1345134534531t", header="qaegheryearhaerheasrseh", footer="asdhrehsdfhdhdrh"))
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()


def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_new_contact(Contact(
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
        app.logout()