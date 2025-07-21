# class Car:
#     def __init__(self, brand: str, model: str, year:int, color: str):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.engine_started = False


#     def start_engine(self):
#         self.engine_started = True
#         print(f"Двигатель запущен для {self.brand} {self.model}")

#     def stop_engine(self):
#         self.engine_started = False
#         print(f"Двигатель остановлен для {self.brand} {self.model}")

#     def print_info(self):
#         print(f"{self.brand} {self.model}, {self.color}")
#         if self.engine_started:
#             print("Двигатель работает")
#         else:
#             print("Двигатель не работает")


# # пример исполользования
# car1 = Car("Toyota", "Camry", 2020, "черный")

# car1.print_info() # до запуска
# car1.start_engine()
# car1.print_info() # после запуска
# car1.stop_engine()
# car1.print_info() # после остановки



class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def area(self)-> int:
        return self.width * self.height
    
    def __eq__(self, obj):
        return self.area() == obj.area()
    
    def __lt__(self, obj):
        return self.area() < obj.area()
    
    def __le__(self, obj):
        return self.area() <= obj.area()
    
    def __gt__(self, obj):
        return self.area() > obj.area()
    
    def __ge__(self, obj):
        return self.area() >= obj.area()
    
    def __ne__(self, obj):
        return self.area() != obj.area()



rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)

print(rectangle1 == rectangle2)  # False
print(rectangle2 == rectangle3)  # True
print(rectangle1 < rectangle2)   # True
print(rectangle2 < rectangle3)   # False
print(rectangle2 <= rectangle3)  # True
