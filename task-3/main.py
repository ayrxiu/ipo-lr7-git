import json
import os

filename = "countries.json"
operations_count = 0

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        countries = json.load(f)
else:
    countries = [
        {
            "id": 1,
            "name": "Минск",
            "country": "Беларусь",
            "is_big": True,
            "people_count":"1.996.730" ,
        },
        {
            "id": 2,
            "name": "Рим",
            "country": "Италия",
            "is_big": True,
            "people_count": "2.200.000",
        },
        {
            "id": 3,
            "name": "Афины",
            "country": "Греция",
            "is_big": True,
            "people_count": "3.300.000",
        },
        {
            "id": 4,
            "name": "Москва",
            "country": "Россия",
            "is_big": True,
            "people_count": "13.274.285",
        },
        {
            "id": 5,
            "name": "Мехико",
            "country": "Мексика",
            "is_big": True,
            "people_count": "689.545",
        },
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)

while True:
    print("\n" + "=" * 50)
    print("꒰ঌ(˶ˆᗜˆ˵)໒꒱")
    print("МЕНЮ:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    print("ヽ(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ")

    choice = input("Выберите пункт меню (1-5): ")

    if choice == "1":
        operations_count += 1
        print("\n" + "=" * 50)
        print("ВСЕ ЗАПИСИ:")
        print("(„ᵕᴗᵕ„)")
        for i, country in enumerate(countries, 1):
            print(f"Запись {i}:")
            print(f"  ID: {country['id']}")
            print(f"  Название города: {country['name']}")
            print(f"  Название страны: {country['country']}")
            print(f"  Большая ли она: {'Да' if country['is_big'] else 'Нет'}")
            print(f"  Население: {country['people_count']}")
            print("( ・∀・)・・・——–☆")

    elif choice == "2":
        operations_count += 1
        try:
            search_id = int(input("Введите ID страны для поиска: "))
            found = False
            for i, country in enumerate(countries):
                if country["id"] == search_id:
                    found = True
                    print(f"\nНайдена запись на позиции {i + 1}:")
                    print(f"Запись {i}:")
                    print(f"  ID: {country['id']}")
                    print(f"  Название города: {country['name']}")
                    print(f"  Название страны: {country['country']}")
                    print(f"  Большая ли она: {'Да' if country['is_big'] else 'Нет'}")
                    print(f"  Население: {country['people_count']}")
                    break
            if not found:
                print("\nЗапись с таким ID не найдена!")
        except ValueError:
            print("\nОшибка: ID должен быть числом!")

    elif choice == "3":
        operations_count += 1
        try:
            new_id = int(input("Введите ID новой страны: "))
            if any(country["id"] == new_id for country in countries):
                print("\n Запись с таким ID уже существует!")
                continue
            name = input("Введите название страны: ")
            country = input("Введите название страны: ")
            is_big_input = input("население города больше 100.000 человек? (да/нет): ").lower()
            is_big = is_big_input in ["да", "yes", "y", "1", "true"]
            people_count = float(input("Введите население этого города в чел: "))

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

    elif choice == "4":
        operations_count += 1
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

    elif choice == "5":
        print(f"\nВсего выполнено операций: {operations_count}")
        print("До свидания! ≽^•⩊•^≼ ")
        break

    else:
        print("\n НЕТ. (ভ_ ভ) ރ ／/ ┊ \＼ Hit the road!")