from sys import maxsize


class Contact:

    def __init__(self,
                 firstname = None,
                 midname = None,
                 lastname = None,
                 nickname = None,
                 title = None,
                 workname = None,
                 homeaddr = None,
                 homephone = None,
                 mobilephone = None,
                 workphone = None,
                 email1 = None,
                 email2 = None,
                 email3 = None,
                 url = None,
                 bday = "1",
                 bmonth = "January",
                 byear = None,
                 aday = "1",
                 amonth = "January",
                 ayear = None,
                 id = None,
                 all_phones_from_home_page= None,
                 all_emails_from_home_page = None
                 ):
        self.firstname = firstname
        self.midname = midname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.workname = workname
        self.homeaddr = homeaddr
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.url = url
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    # отображение объекта в консоли ид:Имя-Фамилия
    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)


    # сравниваем объекты списка контактов по id имени и фамилии
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize