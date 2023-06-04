def show_data():
   with open("book.txt", "r", encoding='utf-8') as file:
        print(file.read())

def add_data() -> None:
    """Добавляет информацию в справочник"""
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    with open("book.txt", "a", encoding='utf-8') as file:
        file.write(f"\n{fio} | {phone}")

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open("book.txt", "r", encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data,data_to_find))

def search(book, info: str):
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    found_contacts = []
    for contact in book:
        if info in contact:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        return 'Совпадений не найдено'
    if len(found_contacts) == 1:
        return found_contacts[0]
    print(*found_contacts, sep='\n')
    more_data_to_find = input('Введите уточняющие данные для поиска: ')
    return search("\n".join(found_contacts), more_data_to_find)

def change_data() -> None:
    """Изменяет информацию в справочнике"""
    data_to_change = input("Введите данные контакта для изменения: ")
    with open("book.txt", "r", encoding='utf-8') as file:
        data = file.read()
    contact_to_change = search(data, data_to_change)
    if contact_to_change == 'Совпадений не найдено':
        print('Совпадений не найдено')
        return
    print("Изменение контакта: ", contact_to_change)
    book = data.split('\n')
    phone = input('Введите новый номер телефона или "del" - для удаления записи: ')
    for i in range(len(book)):
        if book[i] == contact_to_change:
            if phone == "del":
                book.pop(i)
            else:
                book[i] = f"{book[i].split('|')[0]}| {phone}"
    with open("book.txt", "w", encoding='utf-8') as file:
        file.write("\n".join(book))
