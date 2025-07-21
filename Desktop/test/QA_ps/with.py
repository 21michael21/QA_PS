

# Задание 1: Создание простого контекстного менеджера
# Описание:
# Напишите свой собственный контекстный менеджер, который будет открывать и закрывать файл для записи. Используйте методы класса  __enter__ и __exit__.
# Пример использования:
# with FileWriter('example.txt') as file:
#     file.write("Hello, World!")


# class FileWriter:
#     def __init__(self,filename:str):
#         self.filename = filename


#     def __enter__(self):
#         self.file = open(self.filename, 'w')
#         return self.file
    
#     def __exit__(self, type, value, traceback):
#         self.file.close()


# with FileWriter('example.txt') as file:
#     file.write("Hello, World!")




# Задание 2: Контекстный менеджер через contextlib
# Описание:
# Используйте библиотеку contextlib для создания контекстного менеджера, который будет отслеживать время выполнения блока кода и распечатывать его.
# Пример использования:
# import time
# with time_tracker():
#     # Выполнение кода
#     time.sleep(1)



# import time
# from contextlib import contextmanager

# @contextmanager
# def time_tracker():
#     start = time.time()
#     try:
#         yield
#     finally:
#         end = time.time()
#         result = round(end - start)
#         print(f"Время выполнения: {result} секунд")




# with time_tracker():
#     # Выполнение кода
#     time.sleep(1)



## Задание 3: Контекстный менеджер для списка

### Задача:

# Напишите контекстный менеджер на Python для работы со списком, который при выходе из контекста возвращает список в его исходное состояние.

# ### Требования:

# - Написать **две реализации**:
#     1. **С использованием декоратора**.
#     2. **Через класс**.

class ListContextManager:
    def __init__(self,dupl_list:list):
        self.dupl_list = dupl_list

    def __enter__(self):
        self.my_list = self.dupl_list.copy()
        return self.dupl_list
    
    def __exit__(self, type, value, traceback):
        self.dupl_list.clear()
        self.dupl_list.extend(self.my_list)

my_list = [1, 2, 3]
with ListContextManager(my_list) as lst:
    lst.append(4)
    print("Inside context:", lst)  # [1, 2, 3, 4]
print("Outside context:", my_list)  # [1, 2, 3]