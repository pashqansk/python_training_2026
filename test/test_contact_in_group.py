import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group_new(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test-Fname", lastname="test-Lname"))
    if len(orm.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    groups = orm.get_group_list()
    contact = None
    group_id = None
    for group in groups:
        contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
        # добавлять будем рандомный контакт который не вошел  вгруппы
        if contacts_not_in_group:
            contact = random.choice(contacts_not_in_group)
            group_id = group.id
            break
    # создать новый контакт если все уже в группах
    if contact is None:
        new_contact = Contact(firstname="test-Fname", lastname="test-Lname")
        app.contact.create_contact(new_contact)
        # находим созданный контакт и добавляем его в группу
        contact = orm.get_contact_list()[-1]
        group_id = random.choice(groups).id
    app.contact.add_contact_to_group(contact.id, group_id)
    # проверить что контакт добавился
    assert contact in orm.get_contacts_in_group(Group(id=group_id))
    # дополнительный кейс по замечаниям лектора: пытаемся добавить тот же самый контакт в ту же самую группу повторно
    app.contact.add_contact_to_group(contact.id, group_id)
    # !!!Комментарий лектору: бэк здесь имеет правильное поведение и не добавляет контакт в группу повторно,
    # но на UI в этом кейсе пробрасывается необработанное исключение.
    # Если нужно сделать проверку именно UI части и проверять корректное обработку ошибки на UI, то ее нужно делать отдельно.

    # возвращаем ошибку, если контакт повторно добавлен в группу
    if orm.get_contacts_in_group(Group(id=group_id)).count(contact) != 1:
        raise AssertionError("Контакт нельзя добавлять повторно в ту же группу!")


def test_remove_contact_from_group_new(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test-Fname", lastname="test-Lname"))
    if len(orm.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    groups = orm.get_group_list()
    # если есть контакты принадлежащие группам то выбираем любой из них и удаляем его из группы
    groups_with_contacts = []
    for group in groups:
        if len(orm.get_contacts_in_group(group)) > 0:
            groups_with_contacts.append(group)
    if len(groups_with_contacts) > 0:
        group = random.choice(groups_with_contacts)
        contacts_in_group = orm.get_contacts_in_group(group)
        contact_to_remove = random.choice(contacts_in_group)
        app.contact.remove_contact_from_group(contact_to_remove.id, group.id)
        assert contact_to_remove not in orm.get_contacts_in_group(group)
    # если нет контактов принадлежащих группам, то добавляем рандомный контакт в рандомную группу а затем удаляем его из группы
    else:
        all_contacts = orm.get_contact_list()
        contact = random.choice(all_contacts)
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id)
        # проверить что контакт добавился
        assert contact in orm.get_contacts_in_group(group)
        app.contact.remove_contact_from_group(contact.id, group.id)
        # проверить что контакт удалился
        assert contact not in orm.get_contacts_in_group(group)