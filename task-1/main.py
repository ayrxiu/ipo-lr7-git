import math

books = [
    dict(title="Волчья лощина", author="Лорен Уолк", year="2019"),
    dict(title="Сияние", author="Стивен Кинг", year="1977"),
    dict(title="Заводной апельсин", author="Энтони Бёрджесса", year="1962"),
    dict(title="1984", author="Джордж Оруэлл", year="1949"),
    dict(title="Собор Парижской Богоматери", author="Виктор Гюго", year="1831"),
]

for i, book in enumerate(books, start=1):
    print(f"---------------------- Книга {i} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']}")
    
    print(f"-------------------------{book['year']}-------------------------")


