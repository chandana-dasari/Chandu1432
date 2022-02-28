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






