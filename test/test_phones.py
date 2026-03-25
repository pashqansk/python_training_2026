import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# а этот тест теперь не работает, зато первый красивый с лесенкой.
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