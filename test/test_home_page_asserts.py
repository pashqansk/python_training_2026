import re
from random import randrange
from model.contact import Contact

def test_assert_random_credentials_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_edit_page.firstname == contact_from_edit_page.firstname
    assert contact_from_edit_page.lastname == contact_from_edit_page.lastname
    assert contact_from_edit_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_assert_all_credentials_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_home_page_list()
    assert len(contacts_ui) == len(contacts_db)
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)


# TODO с ним надо что-то придумать, т.к. зависим от данных, которые могут обмануть паттерн в регулярке
# TODO потом перенести в другой тестовый файл, работающий с view page
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile


def clean(s):
    return re.sub("[() -]", "", s)

# здесь метод "врот наоборот", следи за руками
def merge_phones_like_on_home_page(contact):
    # 5. то, что осталось после фильтраций - склеивается символом перевода строки
    return "\n".join(
        # 4. если после всего остались пустые строки, то их выбрасываем
        filter(lambda x: x != "",
               # 3. дальше "очищаем" оставшееся от всяких скобок и тире методом clean
               map(lambda x: clean(x),
                   # 2. его фильтруем и выкидываем None
                   filter(lambda x : x is not None,
                          # 1. берем исходный список
                          [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               filter(lambda x: x is not None,
                      [contact.email, contact.email2, contact.email3])))