from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


# параметры ниже можно менять с помощью изменения конфигурации в секции Script parameters, пример -n 10 -f data/test.json
# количество сгенерированных групп
n = 5
# имя файла со сгенерированными данными
f = "data/groups.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# DDT Вариант полного перебора полей
'''group_testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("N***", 10)]
    for header in ["", random_string("H***", 20)]
    for footer in ["", random_string("F***", 20)]]'''

# DDT Окончательный вариант
group_testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("N***", 10),
          header=random_string("H***", 20),
          footer=random_string("F***", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(group_testdata, default=lambda x: x.__dict__, indent=2))