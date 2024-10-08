from books_sdk import get_book_by_id, get_author

print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))

# Гипотеза 1: Неправильные скобки
# Способ проверки: Удалить весь код, кроме скобок, и проверить их количество и порядок
# Установленный факт: получилось ((()))
# Вывод: Гипотеза опроверглась, со скобками всё в порядке

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')
# Установленный факт: Ошибка осталась 
# Вывод: Гипотеза подтвердилась, ошибка находиться во вложеной функции

# Гипотеза 3: Проблема в типе данных, '1' должно быть числом
# Способ проверки: Изменим тип данных у стоки '1', удалим кавычки
# Код для проверки: get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')
# Установленный факт: Ошибка осталась
# Вывод: Гипотеза опроверглась

# Гипотеза 4: Книги с номером 1 не существует
# Способ проверки: Изменим номер книги
# Код для проверки: get_book_by_id(2, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM'); get_book_by_id(3, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')
# Установленный факт: Ошибка осталась
# Вывод: Гипотеза опроверглась, проблема не в номере книги

# Гипотеза 5: Аргументы перепутаны местами
# Способ проверки: Поменяем местами токен и id
# Код для проверки: get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)
# Установленный факт: Код работает
# Вывод: Гипотеза подтвердилась, проблема была в позициях аргументов
