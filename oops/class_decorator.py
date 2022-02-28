#def logging(msg='Hello World', debug=True):
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

#import time
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
import time
# class Outer:
#     def __init__(self, func):
#         self.func = func
#         self.n = 3
#     def __call__(self, *args, **kwargs):
#         print(f"calling {self.func.__name__}")
#         time.sleep(self.n)
#         print("Execution starts")
#         self.func(*args, **kwargs)
#         print("Execution is completed")

# @Outer
# def add(a, b):
#     print(a + b)
# a = add(1, 2)


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

# @Outer
# def add(a, b):
#     print(a + b)
# a = add(1, 2)

# def prices(cls):
#     #print("attaching class attribute")
#     cls.apple = {'iphone': 900, 'ipad': 2800, 'imac': 4500}
#     return cls
# @prices
# class ShoppingCart:
#     def demo(self):
#         print(self.apple)

#def attach_init(cls):


#def spam(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#             #print(res[::-1])
#     return wrapper
#
# def add(a, b):

# def disp(cls):
#     print("hello")


# @disp
# class Spam:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print(f"calling {self.func.__name__}")
#         return self.func(*args, **kwargs)

# @Spam
# class Spam1:
#     def demo(self):
#         print("calling demo")
# s = Spam1()
# s.demo()

#@Spam
# def disp():
#     print("hello")

# d = disp
# print(d)




# import time
# class Record:
#     def __init__(self, func):
#         self.func = func
#         self.n = 3
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         time.sleep(self.n)
#         res = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"delay time is {end-start}")
#         return res
# @Record
# def delay():
#     print("executing delay")
#
# d = delay()







