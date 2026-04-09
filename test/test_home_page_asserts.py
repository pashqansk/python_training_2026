import re
from model.contact import Contact


def test_assert_all_credentials_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page_sorted = sorted(contacts_from_home_page, key=Contact.id_or_max)
    contacts_from_db_sorted = sorted(contacts_from_db, key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page_sorted)):
        contact_from_home_page = contacts_from_home_page_sorted[i]
        contact_from_db = contacts_from_db_sorted[i]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        merged_phones = merge_phones_like_on_home_page(contact_from_db)
        merged_emails = merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merged_phones
        assert contact_from_home_page.all_emails_from_home_page == merged_emails


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