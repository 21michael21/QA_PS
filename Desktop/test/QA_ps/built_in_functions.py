# 1. Квадраты через map
# Описание:
# Напишите функцию squares_map(nums), которая принимает список чисел и возвращает новый список их квадратов, используя map.
# Функции для использования:
# map
# Пример:
# print(squares_map([1, 2, 3, 4]))  # [1, 4, 9, 16]

# def squares_map(nums):
#  return list(map(lambda x: x**2, nums))


# print(squares_map([1, 2, 3, 4]))  # [1, 4, 9, 16]



# 2. Фильтрация чётных через filter
# Описание:
# Напишите функцию filter_even(nums), которая принимает список чисел и возвращает список только чётных, используя filter.
# Функции для использования:
# filter
# Пример:

# print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]3. Сортировка слов двумя способами

# def filter_even(nums):
#  return list(filter(lambda x: x % 2 == 0 , nums))

# print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

 

# 3. Сортировка слов через sorted и list.sort 
# Описание:
# Напишите функцию sort_words(words), которая принимает список строк и возвращает его, отсортированный в алфавитном порядке. Реализуйте два варианта:
# С помощью встроенной функции sorted.
# С помощью метода списка .sort() (не возвращает новый список, а меняет существующий).
# Функции/методы для использования:
# sorted
# list.sort
# Пример:
# print(sort_words(["banana", "apple", "cherry"]))  # ['apple', 'banana', 'cherry']

# def sort_words(words,var:int = 1):
#     if var == 1:
#         return sorted(words)
#     elif var == 2:
#         words.sort()
#         return words
#     else:
#         print("Никак")

# print(sort_words(["banana", "apple", "cherry"], var = 1))
# print(sort_words(["banana", "apple", "cherry"], var = 2))

# 4. Комбинация filter + map
# Описание:
# Напишите функцию square_odds(nums), которая сначала отбирает только нечётные числа (с помощью filter), а затем возвращает список их квадратов (с помощью map).
# Функции для использования:
# filter
# map
# Пример:

# print(square_odds([1, 2, 3, 4, 5]))  # [1, 9, 25]

# def square_odds(nums):
#     return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, nums)))

# print(square_odds([1, 2, 3, 4, 5]))  # [1, 9, 25]



# 5. Накопление результата через functools.reduce
# Описание:
# Напишите функцию product(nums), которая возвращает произведение всех чисел в списке, используя functools.reduce.
# Функции для использования:
# functools.reduce
# Пример:
# print(product([1, 2, 3, 4]))  # 24

# from functools import reduce

# def product(nums):
#     return reduce(lambda x, y: x * y, nums)

# print(product([1, 2, 3, 4]))  # 24


# Методы строк и списков
# 6. Подсчёт слов через split и strip
# Описание:
# Напишите функцию count_words(text), которая принимает строку, убирает пробелы в начале и в конце (strip), разбивает её на слова (split) и возвращает количество слов.
# Методы для использования:
# str.strip
# str.split
# Пример:
# print(count_words("  Hello, world! This is Python.  "))  # 5

# def count_words(text):
#     return len(text.strip().split())

# print(count_words("  Hello, world! This is Python.  "))  # 5

# ​
# 7. Нормализация пробелов через split + join
# Описание:
# Напишите функцию normalize_whitespace(text), которая удаляет лишние пробелы между словами, приводя все последовательности пробелов к одному, используя split и join.
# Методы для использования:
# str.split
# str.join
# Пример:
# print(normalize_whitespace("This   is   a    test"))  # "This is a test"

# def normalize_whitespace(text):
#     return ' '.join(text.split())

# print(normalize_whitespace("This   is   a    test"))  # "This is a test

# 8. Объединение слов в предложение через join
# Описание:
# Напишите функцию make_sentence(words), которая принимает список слов и собирает из них строку-предложение через пробел, используя join.
# Методы для использования:
# str.join
# Пример:
# print(make_sentence(["Python", "is", "fun"]))  # "Python is fun"

# def make_sentence(words):
#     return ' '.join(words)
# print(make_sentence(["Python", "is", "fun"]))  # "Python is fun"

# 9. Расширение списка через extend и альтернативный вариант
# Описание:
# Напишите функцию merge_lists(a, b), которая объединяет два списка. Реализуйте два варианта:
# С помощью метода extend.
# Через оператор +, без использования extend.
# Методы/операторы для использования:
# list.extend
# оператор + для списков
# Пример:
# print(merge_lists([1, 2], [3, 4]))  # [1, 2, 3, 4]

# def merge_lists(a, b):
#     a_copy = a[:]
#     a_copy.extend(b)
#     return a_copy


# def merge_lists_alt(a, b):
#     return a + b

# print(merge_lists([1, 2], [3, 4]))  # [1, 2, 3, 4]
# print(merge_list_alt([1, 2], [3, 4]))  # [1, 2, 3, 4]

# 10. Удаление элементов через pop
# Описание:
# Напишите функцию pop_until_zero(nums), которая принимает список чисел и последовательно извлекает (pop) элементы с конца до тех пор, пока не встретит 0, и возвращает список извлечённых элементов (без самого нуля).
# Метод для использования:
# list.pop
# Пример:
# print(pop_until_zero([5, 3, 1, 0, 7, 8]))  # [8, 7]

# def pop_until_zero(nums):
#     result = []
#     while nums and nums[-1] != 0:
#         result.append(nums.pop())
#     return result

# print(pop_until_zero([5, 3, 1, 0, 7, 8]))  # [8, 7]

# В каждой задаче указано, какие встроенные функции или методы нужно применять. Можно добавлять и свои вариации решений через другие подходящие функции (например, filter вместо reduce или генераторы списков), но в описании подчёркнута обязательная функция.
# 11. Трансформация значений словаря через map + lambda
# Описание:
# Напишите функцию double_dict_values(d), которая принимает словарь d с числовыми значениями и возвращает новый словарь, в котором каждое значение умножено на 2. Используйте map вместе с lambda.
# Функции для использования:
# map
# lambda
# Пример:
# print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))
# # {'a': 2, 'b': 4, 'c': 6}

# def double_dict_values(d):
#     return dict(map(lambda item: (item[0], item[1]*2), d.items()))

# print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))
# # {'a': 2, 'b': 4, 'c': 6}

# ### 12. Фильтрация словаря через `filter` + `lambda`

# **Описание:**

# Напишите функцию `filter_dict_by_value(d, threshold)`, которая принимает словарь `d` и число `threshold`, и возвращает новый словарь, содержащий только те пары, у которых значение больше `threshold`. Используйте `filter` вместе с `lambda`, а затем соберите результат обратно в словарь.

# **Функции для использования:**

# - `filter`
# - `lambda`
# - преобразование `dict(...)`

# **Пример:**

# ```python
# print(filter_dict_by_value({'x': 10, 'y': 3, 'z': 7}, 5))
# # {'x': 10, 'z': 7}
# ```

# def filter_dict_by_value(d, threshold):
#     return dict(filter(lambda item: item[1] > threshold, d.items()))

# ```python
# print(filter_dict_by_value({'x': 10, 'y': 3, 'z': 7}, 5))
# # {'x': 10, 'z': 7}

# ### 13. Сортировка списка словарей через `sorted` + `lambda`

# **Описание:**

# Напишите функцию `sort_people_by_age(people)`, где `people` — список словарей с ключами `'name'` и `'age'`. Функция должна возвращать новый список, отсортированный по полю `'age'` по возрастанию, используя `sorted` с ключом-`lambda`.

# **Функции для использования:**

# - `sorted`
# - `lambda`

# **Пример:**

# ```python
# people = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob',   'age': 25},
#     {'name': 'Carol', 'age': 35}
# ]
# print(sort_people_by_age(people))
# # [
# #   {'name': 'Bob',   'age': 25},
# #   {'name': 'Alice', 'age': 30},
# #   {'name': 'Carol', 'age': 35}
# # ]
# ```

# def sort_people_by_age(people):
#     return sorted(people, key=lambda person: person['age'])

# people = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob',   'age': 25},
#     {'name': 'Carol', 'age': 35}
# ]
# print(sort_people_by_age(people))
# # [
# #   {'name': 'Bob',   'age': 25},
# #   {'name': 'Alice', 'age': 30},
# #   {'name': 'Carol', 'age': 35}
# # ]

# ### 14. Сортировка ключей и значений словаря через `sorted`

# **Описание:**

# Напишите две функции:

# 1. `sorted_dict_keys(d)` — возвращает список ключей `d` в отсортированном порядке.
# 2. `sorted_dict_items_by_value(d)` — возвращает список кортежей `(key, value)`, отсортированных по значению, используя `sorted`.

# **Функции для использования:**

# - `sorted`

# **Пример:**

# ```python
# d = {'b': 2, 'a': 1, 'c': 3}
# print(sorted_dict_keys(d))            # ['a', 'b', 'c']
# print(sorted_dict_items_by_value(d))  # [('a', 1), ('b', 2), ('c', 3)]
# ```

# def sorted_dict_keys(d):
#     return sorted(d.keys())

# def sorted_dict_items_by_value(d):
#     return sorted(d.items(), key=lambda item: item[1])

# d = {'b': 2, 'a': 1, 'c': 3}
# print(sorted_dict_keys(d))            # ['a', 'b', 'c']
# print(sorted_dict_items_by_value(d))  # [('a', 1), ('b', 2), ('c', 3)]

# ### 15. Комбинированное задание: `map` + `filter` + `sorted`

# **Описание:**

# Напишите функцию `process_numbers(nums)`, которая:

# 1. С помощью `filter` и `lambda` отбирает чётные числа.
# 2. С помощью `map` и `lambda` возводит их в квадрат.
# 3. Возвращает готовый список, отсортированный по убыванию, с помощью `sorted(..., reverse=True)`.

# **Функции для использования:**

# - `filter`
# - `map`
# - `sorted`
# - `lambda`

# **Пример:**

# ```python
# print(process_numbers([5, 2, 7, 4, 1, 8]))  # [64, 16, 4]
# ```


def process_numbers(nums):
    return sorted(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)), reverse=True)

print(process_numbers([5, 2, 7, 4, 1, 8]))  # [64, 16, 4]