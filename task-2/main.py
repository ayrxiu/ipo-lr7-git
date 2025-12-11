import json
with open("dump.json", "r", encoding="utf - 8") as f:
    a = json.load(f)
    qualiti = input("Введите номер квалификации: ").strip()
    for word in a:
        if word.get("model") == "data.skill":
            if word.get("fields", {}).get("code") == qualiti:
                print(f"======================== Найдено ==========================")
                print(f"{word["fields"]["title"]}")
                break
            else:
                print("===========================Не найдено ============================")
                break