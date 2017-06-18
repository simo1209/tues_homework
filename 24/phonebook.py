import json
import os.path
import sys


def load_contacts_from_file(filename):
    if os.path.exists(filename):
        f = open(filename)
        contacts = json.loads(f.read())
        f.close()
    else:
        contacts = []
    return contacts

def save_contacts_to_file(filename, contacts):
    f = open(filename, 'w')
    f.write(json.dumps(contacts))
    f.close()


def set_phone(filename, name, phone):
    """
    Задава телефонен номер `phone` на човек с име `name`.
    Ако съществува човек с име `name` променя телефона му.
    Ако не съществува - добавя нов запис в телефонния указател.
    Функцията трябва да:
        - прочете указателя от файла с име `filename`
        - модифицаира указателя
        - запише указателя във файла с име `filename`
    Пример:
    >>> set_phone('phonebook.json', 'Ivan', '0895-11-11-11')  # doctest: +SKIP
    """
    contacts = load_contacts_from_file(filename)
    index = find_contact_index(contacts, name)
    if index != -1:
        contacts[index]['phone'] = phone
    else:
        insert_contact(contacts, name, phone)
    save_contacts_to_file(filename, contacts)


def remove_phone(filename, name):
    """
    Изтрива записа (ако цъществува) за човек с име `name` от телефонния указател.
    Функцията трябва да:
        - прочете указателя от файла с име `filename`
        - модифицаира указателя
        - запише указателя във файла с име `filename`
    Пример:
    >>> remove_phone('phonebook.json', 'Ivan')  # doctest: +SKIP
    """
    contacts = load_contacts_from_file(filename)
    index = find_contact_index(contacts, name)
    if index != -1:
        contacts.pop(index)
    save_contacts_to_file(filename, contacts)


def find_phone(filename, name):
    """
    Намире телефонния номер на човек с име `name`.
    Връща като резултат телефонния номер или `None` ако не го открие.
    Функцията трябва да:
        - прочете указателя от файла с име `filename`
        - потърси и върне телефонния номер
    Пример:
    >>> find_phone('phonebook.json', 'Ivan')  # doctest: +SKIP
    '0895-11-11-11'
    """
    contacts = load_contacts_from_file(filename)
    index = find_contact_index(contacts, name)
    if index != -1:
        return contacts[index]['phone']
    else:
        return "None"


def find_contact_index(contacts, name):
    """
    Функция, която намира позицията на контакт в списъка (по име).
    Връща като резултат пизицията или `-1`, ако не успее да намери контакт с такова име.
    >>> contacts = [{'name': 'Pesho', 'phone': 1}, {'name': 'Gosho', 'phone': 2}]
    >>> find_contact_index(contacts, 'Gosho')
    1
    >>> find_contact_index(contacts, 'Ivan')
    -1
    """
    res=-1
    i=0
    while i<len(contacts):
        if contacts[i]['name']==name:
            res=i
        i+=1
    return res
    pass


def insert_contact(contacts, name, phone):
    contacts.append({'name':name,'phone':phone})
    """
    Функция, която вмъква нов контакт в списъка с контакти,
    като запазва списъка сортиран по име.
    >>> contacts = []
    >>> insert_contact(contacts, 'Pesho', 1)
    >>> insert_contact(contacts, 'Gosho', 2)
    >>> contacts[0]['name']
    'Gosho'
    >>> contacts[1]['name']
    'Pesho'
    >>> insert_contact(contacts, 'Boby', 3)
    >>> contacts[0]['name']
    'Boby'
    >>> contacts[1]['name']
    'Gosho'
    >>> contacts[2]['name']
    'Pesho'
    >>> insert_contact(contacts, 'Tosho', 4)
    >>> contacts[3]['name']
    'Tosho'
    """
    contacts.sort(key=lambda x:x['name'])
    return contacts
    pass

'''
def do_command(command, *args):
    result = {
        'set': set_phone,
        'remove': remove_phone,
        'find': find_phone
    }[command](*args)
    if result:
        print(result)


if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'test':
        import doctest
        doctest.testmod()
    else:
        do_command(*sys.argv[1:])
'''
print(find_phone('phonebook.json', 'Ivan'))