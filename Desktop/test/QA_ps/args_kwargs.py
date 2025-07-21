

# def sum_all(*args):
#     count = 0 
#     for i in args:
#         count += i
#         lenght_args = len(args)
        
#     return count, lenght_args

# result = sum_all(3,454,65,43,2,32,443,54,43 )

# print(f" первым числом сумма всех числел, вторрым колличество: {result}")


# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

    
# # Пример вызова
# greet(name="John", age=30, city="New York")


def greet(**kwargs):
   if 'name' in kwargs:
      print(f"Hello, {kwargs['name']}!")
   else:
      print("Hello!")


greet(name="John", age=30, city="New York")