from model.group import Group


def test_add_group(app, data_groups):
        old_groups = app.group.get_group_list()
        group = data_groups
        app.group.create_group(group)
        # проверяем что новая группа добавлена. сверяется длина старого списка с общим количеством групп
        # count() выступает в качестве хэша
        assert len(old_groups) + 1 == app.group.count()
        # загружаем список групп
        new_groups = app.group.get_group_list()
        # добавляем ту же группу в список old_groups
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''@pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create_contact(contact)
        # сюда тоже сверку с хэшем можно прикрутить, т.к. метод уже существует
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        # добавляем ту же группу в список old_groups
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)'''