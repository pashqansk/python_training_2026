from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


# параметры ниже можно менять с помощью изменения конфигурации в секции Script parameters, пример -n 10 -f data/test.json
# количество сгенерированных контактов
n = 5
# имя файла со сгенерированными данными
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


contact_testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("FN", 10),
            middlename=random_string("MN", 10),
            lastname=random_string("LN", 10),
            nickname=random_string("NN", 10),
            title=random_string("TI", 20),
            company=random_string("WORK", 10),
            address=random_string("ADDR", 20),
            home=random_string("HPh", 5),
            mobile=random_string("MPh", 10),
            work=random_string("WPh", 15),
            email=random_string("E1", 5),
            email2=random_string("E2", 10),
            email3=random_string("E3", 15),
            homepage=random_string("URL", 20),
            bday="1",
            bmonth="January",
            byear="1995",
            aday="1",
            amonth="January",
            ayear="2025"
            )
    for n in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(contact_testdata))