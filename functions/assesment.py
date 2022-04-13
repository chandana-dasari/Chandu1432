# a = 10
# def fun1():
#     a += 20
#
#
#     # def inner():
#     #     nonlocal a
#     #     a += 10
# fun1()
# print(a)

# d1 = {'one': 1, 'Two': 2, 'three': 3, 'four': 4}
# d2 = {'three': 5, 'Five': 5, 'Two': 4}
# print(d1 +d2)

# s = 'AABBCCCDAACD'
# s1 = ''
# b = 0
# count = 1
# for i in range(b, len(s)):
#     if s.charAt(b) != s.charAt(b + 1) and count = 1
#     count = 0
#
#     for j in s[b:len(s)]:
#         b += 1
#         if i == j:
#             count += 1
#         else:
#             break


# def anagram(a, b):
#     count = 0
#     for i in a:
#         if i in b:
#             count += 1
#     if len(a) == count:
#         print("Anagram each other")
#     else:
#         print("not anagram")
#
#
# anagram('hat', 'eat')


#s  = 'aabbcccdaacd'
# s2 = list(s)
# print(s2)
# s1 = ''
# #count = 0
# for i in enumerate(:
#     count = 0
#     for j in s2:
#         #count = 0
#         if i == j:
#             count += 1
#             s1 = str(count) + j
#
#     print(s1, end='')
# s = 'abbbccrrr'
# i = 0
# count = 0
# res = ''
# while i <len(s):
#     if s[i] == s[i+1:i+2]:
#         count += 1
#         i += 1
#     else:
#         count += 1
#         res += str(count) + s[i]
#         count = count - count
#         i += 1
# print(res)


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

#print(sub(5,3))

#
# d = {'a':190, 'b':543, 'c':243, 'd': 133, 'e':334}
# import re
# a = []
# for key, value in d.items():
#     var = str(value)
#     a.append(re.findall(r'\d', var))
# #print(a)
# b = []
# for item in a:
#     b.append(''.join(item))
# print(b)
# c = sorted(b, key=lambda ele : int(ele))
# print(c)
# print(c[0])


# pat = ''
# n = 'a'
# m = 'e'
# for i in range(ord(n), ord(m)+1):
#     pat = pat + ' '+ str(chr(i))
#     print(f'{pat:^10}')

# n = 5
# for i in range(0, n):
#     for j in range(0, n-i+1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()

# n = 5
# # i =0
# # j = 0
# for i in range(0, n):
#     for j in range(1, n+1):
#         if i+j <= n+1 and i >= j:
#             print("*", end=" ")
#         elif i+j >= n+1 and i <= j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#    print()
#i/p is "python@#$%pool"
# o/p should be ['PYTHON', 'POOL']


# n = "python@#$%pool"
# import re
# a = re.findall(r"\w+", n)
# print(a)
# li = [item.upper() for item in a]
# print(li)
#
#  Write a program to print all the number which are ending with 5

# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# import re
# for num in numbers:
#     match = re.findall(r"^5", num)
#     if match:
#         print(num)
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# #output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
# print(dd)

#Write a program to print all the words which starts with letter 'h' in the given string
# st = 'hai hello how are you what are you doing'
# import re
# li = st.split()
# for word in li:
#     match = re.findall(r'^h\w+', word)
#     if match:
#         print(word)
#
# Write a program to sum all even numbers in the given string

# sentence = 'hello 123 world 567 welcome to 9724 python'
# import re
# match = re.findall(r"\d", sentence)
# print(match)
# li = [int(num) for num in match]
# print(li)
# even_ = [i for i in li if i % 2 == 0]
# print(even_)
# sum = 0
# for j in even_:
#     sum += j
# print(sum)
#  Write a program to add each number in word1 to number in word2
#
# # e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9
# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# import re
# a = re.findall(r"\d", word1)
# b = re.findall(r"\d", word2)
# total = []
# for i, j in zip(a, b):
#     total.append([i,j])
# print(total)


#120 Write a program to print all the number which are starting with 8

# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# li = []
# import re
# for num in numbers:
#     match = re.findall(r"^8\d", num)
#     if match:
#         print(match)

# 121
# Write
# a
# program
# to
# remove
# duplicates
# from the list
#
# without
# using
# set or empty
# list

# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1[::]         #l1.copy()
# print(l2)
# for num in l2:
#     if l1.count(num)>1:
#         l2.remove(num)
# print(l2)
# Print all the missing numbers from 1 to 10 in the below list

# numbers = [1, 3, 6, 8, 10]
# for i in range(1, 11):
#     if i not in numbers:
#         print(f"missing number {i}")
#
# Write a python program to get the below output

# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
# res = [''.join((str(x), y)) for x in l1 for y in l2]
# print(res)

#Write a python program to get the below output

#word = "AAAAaaccYYY"  # o/p ['Y3', 'c2', 'A4', 'a2']
# se = set(word)
# li = list(se)
# res = [''.join((i, str(word.count(i)))) for i in li[::-1]]
# print(res)

 # Get all the unique characters
# unique_letters = set(word)
#
# # build a list of character and its count pair
# count = [''.join((letter, str(word.count(letter)))) for letter in unique_letters]
# print(count)
#['Y3', 'c2', 'A4', 'a2']

#In the list below, find all the number pairs which results in 10 either when added or subtracted

# a = [3, 5, -4, 8, 11, 1, -1, 6]
# for item1 in a:
#     for item2 in a:
#         if item1 != item2:
#             if item1 + item2 == 10 or item1 - item2 == 10:
#                 print((item1, item2))
#Write a decorator to prefix +91 to the original phone numbers
# numbers = [1234567890, 123456790, 1234567890]
# def prefix_num(func):
#     def wrapper(*args, **kwargs):
#         numbers = args[0]
#         res = ["+91" + str(num) for num in numbers]
#         return res
#     return wrapper
# @prefix_num
# def _prefix(numbers):
#     for number in numbers:
#         print(number)
# print(_prefix(numbers))


#128 Write a program to get the below output

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# # o/p should be ['b', 'd']
# key = d.keys()
# keys = list(key)
# k = []
# for key in keys[1::2]:
#     k.append(key)
# print(k)

# class Parent:
#     @staticmethod
#     def demo():
#         print("method in parent class")
# class Child(Parent):
#     @staticmethod
#     def demo():
#         print("method in child class")
#
# c = Child()
# c.demo()
#
#
# # for k in key[::2]:
# #     print(k)


#MULTITHREADING
# def timer(func):
#     def inner():
#         import time
#         st = time.time()
#         print(st)
#         end = time.time()
#         print(end)
#         print(f"The total time taken is {end-st}")
#     return inner
# @timer
# def sqr():
#     for i in range(1, 21):
#         i = i ** 2
# import threading
# t1 = threading.Thread(target = sqr, args = ())
# t1.start()
# t1.join()
#
# n = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# for i in range(1, len(n)+1):
#     if i not in n:
#         print(f"missing num {i}")
#n = [12, 34, 56, 78]
# def swap(list):
#     size = len(list)
#     temp = list[0]
#     list[0] = list[size-1]
#     list[size-1] = temp
#     return list
# print(swap(n))
# Min, *rest, max = n
# m = list(max, *rest, Min)
# print(m)


# n = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in n[1:len(n):2]:
#     print(i)

# li = ['hi', 'hello', 'hi', 'how', 'hi', 'are', 'you']
# from collections import defaultdict, Counter
# # d = defaultdict(int)
# # for i in li:
# #     d[i] += 1
# # print(d)
# c = Counter(li)
# print(c.most_common())


# n = 8
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime")
#     else:
#         print("prime")

# def tail(li, n):
#     if not isinstance(n, int):
# def tail(iterable, n):
#     if not isinstance(n, int):
#         raise TypeError('Value of n should be Positive Integer')
#     if n <= 0:
#         return ()
#     return tuple(iterable)[-n:]
# print(tail((2, 3, 4, 5, 6), 2))

# from math import sqrt
# def is_perfect_square(num):
#     return num == sqrt(num) ** 2
# print(is_perfect_square(25))

# n = 50
# for n in range(50):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("not prime")
#                 continue
#         else:
#             print(n)
# n = 4
# for i in range(2, n):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# a = 'hworldddd'
# for i in a:
#     if a.count(i) > 1:
#         print(i)
#         break

# sen = 'hello world welcome to python hello how are you'
# n = 2
# import re
#
# def index_nth_occurance(sentence, pat, n):
#     matches = re.finditer(pat, sentence)
#     _count = 0
#     for match in matches:
#         _count +=1
#         if _count == n:
#             return f"Start Index: {match.start()}, End Index: {match.end()}"
# print(index_nth_occurance(sen, 'hello', 2))

# a = [10, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
# def series(iter1, iter2):
#     diff = iter1[1] - iter1[0]
#     c = iter1 + iter2
#     return all([True if c[i]+diff == c[i+1] else False for i in range(0, len(c)-1)])
#
# print(series(a, b))

# n = "hello(&*())(*&^hier"
# from collections import defaultdict
# d = defaultdict(int)
# for i in n:
#     if i.isalnum():
#         d[i] += 1
# print(d)

# s = "hi there! how are you:) how"
# import re
# a = re.findall(r"\b\w+", s)
# print(a)

# numbers = [23, 3, 54, 56, 6, 6, 6, 56]
# a = max(numbers)
# for n in numbers:
#     if n == a:
#         print(n)

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# def rotate(name, n):
#     for i in range(n):
#         l = name.pop()
#         name.insert(0, l)
#     return name
# print(rotate(items, 3))

# st = 'chandana'
# def rotate(char, n):
#     li = list(char)
#     print(li)
#     for i in range(n):
#         ele = li.pop()
#         li.insert(0, ele)
#     return ''.join(li)
# print(rotate('chandana', 2))


# def rotate_string(string, n):
#     string = list(string)
#     for _ in range(n):
#         f = string.pop()
#         string.insert(0, f)
#     return ''.join(string)
# print(rotate_string('chandana', 2))

# d = {'a': 1, 'b': 2, 'c': 3}
# d1 = {}
# for key, value in d.items():
#     d1[value] = key
# print(d1)
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i+j <= n+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i+j >= n+1 and i >= j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#Polymorphism
# class Demo:
#     def display(self):
#         print("hello world")
# class Demo1(Demo):
#     def display(self):
#         print("hello everyone")
#         print("how are you")
# d = Demo1()
# d.display()


#from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
# class Human(Animal):
#     def disp(self):
#         print("I can walk and run")
# class Dog(Animal):
#     def disp(self):
#         print("I can bark")
# h = Human()
# h.disp()
# d = Dog()
# d.disp()
# path=r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#     #print(file)
#     count = 0
#     for line in file:
#         #print(line)
#         word = line.split()
#         #print(word)
#         for i in word:
#             li = list(i)
#             #print(li)
#             for j in li:
#                 #print(j, end=' ')
#                 if 'A' <= j <='Z':
#                     count += 1
#                     #print(j)
#     print(count)
# import re
# s = 'dasarichan.dana111@yahoo.com'
# match = re.findall(r"^(.+)@(\S+)$", s)
# if match:
#     print(match)
# else:
#     print("False")
# else:
#     print("not match")





# import re
# s = '234567)(*)_)'
#
# match = re.findall(r"\S+@\S+", s)
# if match:
#     print(match)
# else:
#     print("enter valid email")

# from os import *
# # import os
# print(getcwd())

# a = '19.34.56.90'
# li = a.split('.')
# print(li[::-1])

# class Demo:
#     def animal():
#         print("inside animal")
#     def human(self):
#         print("inside human")
#         d = Demo()
# print(d.animal)
# d.human()

# s = 'chandana'
# def rotate(name, n):
#     li = list(name)
#     for i in range(n):
#         ele = li.pop()
#         li.insert(0,ele)
#     return ''.join(li)
#
# print(rotate(s, 2))
#
# l = ['apple', 3, 5, 'python', 56]
# def rotate(name, n):
#     for i in range(n):
#         l = name.pop()
#         name.insert(0, l)
#     return name
# print(rotate(l, 2))

# li = [12, 34, 56, 78]
# min, *rest, max = li
# l2 = [max, *rest, min]
# print(l2)

# d = {'a': 10, 'b': 20}
# for k, v in d.items():
#     print((k, v))
#     print(K)

# d = {(10, 20): 10, (30, 40): 20, (50, 60): 30}
# for key in d.keys():
#     print(*key)
#     print(sorted(key))

# l = ['a', 'b', 'c']
# d = dict.fromkeys(l, None)
# print(d.popitem())
# l = [4, 5, 6, 7, 8, 9]
# l1 = []
# for i in range(len(l)-1, -1, -1):
#     print(l[i])
# s = ({'a':1, 'b':2}, [2, 4, 5])
# a = len(s)
# print(a)
# n = 5
# i = 1
# fact = 1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(fact)

# #0,1,1,2,3,5,8
# def fib(n, a=0, b=1, i=0):
#     while i < n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#         i = i+1
# fib(10)

# def is_anagram(s1, s2):
#     if s1.upper() == s2.upper():
#         return False
#     st1 = sorted(s1.upper())
#     st2 = sorted(s2.upper())
#     if st1 == st2:
#         return True
#     else:
#         return False
#
# print(is_anagram('eat', 'hate'))


# from collections import defaultdict
# l = ['ate', 'hello', 'eat', 'who', 'how']
# d = defaultdict(list)
# for word in l:
#     s = ''.join(sorted(word))
#     d[s].append(word)
# print(d)


# n = 234
# print(n % 10)
# s = str(n)
# print(s[-1])

# n = 7
# for n in range(50):
#     if n > 1:
#         for i in range(2, n):
#                 if n % i == 0:
#                     print("not prime")
#                     break
#         else:
#             print(n)

# n = 153
# s = str(n)    #'153'
# b = len(s)    #3
# a = 0
# for i in s:
#     c = int(i) ** b
#     a += c
# #print(a)
# if a == n:
#     print("anagram")
# else:
#     print("not anagram")

# class Sample:
# 	a = 10
# 	b = 20
# 	a, b = b, a
# s = Sample()
# print(s.a)
# print(s.b)
#
# def spam(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# @spam
# def even(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "not even"
# e = even(7)
# print(e)
# import re
# res = re.findall(r"[^0-9A-Z]{8,10}", 'hai$hellootgyhjkm')
# print(res)

# from dataclasses import dataclass
# @dataclass
# class Article:
#     title:str
#     author:str
#     language:str
#
# a = Article("Pycharm", "Guidovanrassum", "Python")
# b = Article("pip", "Guido", "Ruby")
# print(a == b)

# a = 'hai'
# r = ''
# for i in a:
#     r = i + r
# print(r)

# s = 'hai'
# for index, item in enumerate(s):
#     print((index, item))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         res1 = []
#         print(args)
#         for i in args[0]:
#             if i % 2 == 0:
#                 res1.append(i)
#         return res1
#     return wrapper
# @outer
# def even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "False"
# print(even(4))
# print(add(2, 3))
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i + j > n-1:
#             print('*', end=' ')
#         else:
#             print(" ", end=" ")
#     print()
# class Emp:
#     __id= 458
#     def __name__(self,name):
#         print(self.name)
# print(Emp.__dict__)

# l = [3, 6, 7, 8, 2]
# l1 = sorted(l)
# print(sorted(l, reverse = True))
# print(l1[-2])












































# s = 'we@2#$3%6^1yhgf67987dg'
# import re
# print(re.findall(r"\W",s))
# s = 'haai 1834 %hello243'
# import re
# match = re.findall(r"\d", s)
# count = 0
# for num in match:
#     count += 1
# print(count)
# a = [[1, 2, 3], [6, 5, 7]]
# inter = [sum(i) for i in a]
# print(inter)
# count = 0
# for i in a:
#     #print(i)
#     for num in i:
#         count += num
# print(count)
# d = {'a': 1, 'b': 2}
# d1 = {'c': 4, 'd': 5}
# d2 = {**d, **d1}
# print(d2)









