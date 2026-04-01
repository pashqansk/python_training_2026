from model.group import Group
import random
import string


group_const = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


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
    for i in range(5)
]

