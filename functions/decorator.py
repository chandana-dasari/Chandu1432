#executing function for 3 times

# def spam(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#             #print(res[::-1])
#     return wrapper
#
# def add(a, b):


# import time
# def outer(n):
#      def delay(func):
#          def wrapper(*args, **kwargs):
#              time.sleep(n)
#              print("execution starts")
#              func(*args, **kwargs)
#              print("execution is completed")
#          return wrapper
#      #print("execution is completed")
#      return delay

# @outer(2)
# def add(a, b):
#     print(a + b)
# add(4, 5)
# @outer(5)
# def exp(a, b):
#     print(a * b)
# exp(4, 4)


# num = [ 1234567890, 9123456789, 911234567890, 119234567810 ]
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith('91'):
#         str_number = '+' + str_number[:2] + '-' + str_number[2:]
#         return str_number
#     else:
#         return str_number
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(num) for num in temp]
#         return func(processed_numbers)
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(phone_numbers):
#     for item in phone_numbers:
#         print(item)
#
# print_numbers(num)


# def spam(*names):
#     def _spam(func):
#         def wrapper(*args, **kwargs):
#             print(names)
#             return func(*args, **kwargs)
#         return wrapper
#     return _spam
# @spam('steve', 'jobs', 'dhana')
# def add(a, b):
#     return a+b
#
# print(add(4,4))

# def logging(msg='Hello World', debug=True):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             if debug:
#                 print(msg, func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return log
#
# @logging('hai')   #sub = logging(sub)
# def sub(a, b):
#     return a+b
#
# print(sub(5,3))


# def _div(func):
#     def wrapper(*args, **kwargs):
#         a, b = args
#         res = func(*args, **kwargs)
#         if b == 0:
#             return f"{b} cannot be a divisor"
#         return res
#     return wrapper
# def div(a, b):
#     return a/b
#
# d = div(a = 6, b = 2)
# print(d)












