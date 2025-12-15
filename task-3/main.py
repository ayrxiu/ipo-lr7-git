import json

def add_country(countries, filename, new_id, name, country, is_big, people_count):
    try:
        new_country = {
            "id": new_id,
            "name": name,
            "country": country,
            "is_big": is_big,
            "people_count": people_count,
        }
        countries.append(new_country)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(countries, f, ensure_ascii=False, indent=2)
        print("\nЗапись успешно добавлена!")
    except ValueError:
        print("\nОшибка ввода данных!")

def delete_country(countries, filename):
    try:
        delete_id = int(input("Введите ID страны для удаления: "))
        found = False
        for i, country in enumerate(countries):
            if country["id"] == delete_id:
                found = True
                del countries[i]
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(countries, f, ensure_ascii=False, indent=2)
                print("\nЗапись успешно удалена!")
                break
        if not found:
            print("\nЗапись с таким ID не найдена!")
    except ValueError:
        print("\nОшибка: ID должен быть числом! ¯\_(ᵕ—ᴗ—)_/¯")

def exit_program(operations_count):
    print(f"\nВсего выполнено операций: {operations_count}")
    print("До свидания! ≽^•⩊•^≼ ")

def invalid_choice():
    print("\n НЕТ. (ভ_ ভ) ރ ／/ ┊ \＼ Hit the road!")

def menu():
    print("\nМеню:")
    print("1. Добавить страну")
    print("4. Удалить страну")
    print("5. Выход")

def main():
    filename = "countries.json"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            countries = json.load(f)
    except FileNotFoundError:
        countries = []

    operations_count = 0

    while True:
        menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            operations_count += 1
            new_id = int(input("Введите ID: "))
            name = input("Введите название: ")
            country = input("Введите страну: ")
            is_big = input("Большая страна? (да/нет): ")
            people_count = int(input("Введите количество людей: "))
            add_country(countries, filename, new_id, name, country, is_big, people_count)

        elif choice == "4":
            operations_count += 1
            delete_country(countries, filename)

        elif choice == "5":
            exit_program(operations_count)
            break

        else:
            invalid_choice()

if name == "main":
    main()
        print("До свидания! ≽^•⩊•^≼ ")
        break

    else:
        print("\n НЕТ. (ভ_ ভ) ރ ／/ ┊ \＼ Hit the road!")
