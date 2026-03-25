import re
from random import randrange


def test_assert_random_credentials_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_edit_page.firstname == contact_from_edit_page.firstname
    assert contact_from_edit_page.lastname == contact_from_edit_page.lastname
    assert contact_from_edit_page.homeaddr == contact_from_edit_page.homeaddr
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

# TODO с ним надо что-то придумать, т.к. зависим от данных, которые могут обмануть паттерн в регулярке
# TODO потом перенести в другой тестовый файл, работающий с view page
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone


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
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clean(x),
                     filter(lambda x: x is not None,
                            [contact.email1, contact.email2, contact.email3]))))