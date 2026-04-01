from string import punctuation
from model.contact import Contact
import random
import string


contact_const = [
    Contact(firstname="fname1",
            midname="midname1",
            lastname="lastname1",
            nickname="nickname1",
            title="title1",
            workname="workname1",
            homeaddr="homeaddr1",
            homephone="homephone1",
            mobilephone="mobilephone1",
            workphone="workphone1",
            email1="email1",
            email2="email2",
            email3="email3",
            url="url1",
            bday="1",
            bmonth="January",
            byear="1995",
            aday="1",
            amonth="January",
            ayear="2025")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


contact_testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("FN", 10),
            midname=random_string("MN", 10),
            lastname=random_string("LN", 10),
            nickname=random_string("NN", 10),
            title=random_string("TI", 20),
            workname=random_string("WORK", 10),
            homeaddr=random_string("ADDR", 20),
            homephone=random_string("HPh", 5),
            mobilephone=random_string("MPh", 10),
            workphone=random_string("WPh", 15),
            email1=random_string("E1", 5),
            email2=random_string("E2", 10),
            email3=random_string("E3", 15),
            url=random_string("URL", 20),
            bday="1",
            bmonth="January",
            byear="1995",
            aday="1",
            amonth="January",
            ayear="2025"
            )
    for n in range(5)
]