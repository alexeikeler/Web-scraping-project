import numpy as np


class BookTypes:

    AMOUNT: int = 10

    TYPES: np.ndarray = np.array([
        'Художественная литература', 'Словари и энциклопедии',
        'Учебники', 'Научная и техническая литература',
        'Дом и хобби', 'Путешествия и спорт',
        'Бизнес литература', 'Религия и эзотерика',
        'Книги для родителей', 'Комиксы'
    ])

    CHARACTERISTICS: np.ndarray = np.array([
        'Раздел',
        'Автор', 'Литература по странам',
        'Литература по периодам', 'Год издания',
        'Издательство', 'Формат книги',
        'ISBN', 'Язык', 'Переплет',
        'Иллюстрации', 'Количество страниц',
    ])

    LINKS: np.ndarray = np.array([
        'https://rozetka.com.ua/hudojestvennaya-literatura/c4326593/',
        'https://rozetka.com.ua/slovari-spravochniki-entsiklopedii/c4326635/',
        'https://rozetka.com.ua/uchebniki-nauchno-metodicheskaya-literatura/c4326656/',
        'https://rozetka.com.ua/tehnicheskaya-literatura-instruktsii-rukovodstva/c4326663/',
        'https://rozetka.com.ua/dlya-doma-i-byta-krasoty-i-zdorovya/c4326677/',
        'https://rozetka.com.ua/dosug-hobbi-sport/c4619871/',
        'https://rozetka.com.ua/knigi-dlya-biznesa/c4620235/',
        'https://rozetka.com.ua/religiya-ezoterika/c4625307/',
        'https://rozetka.com.ua/books-for-parents/c4626644/',
        'https://rozetka.com.ua/komiksi/c4648794/'
    ])
