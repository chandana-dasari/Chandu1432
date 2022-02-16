# def reve(a):
#     for char in range(len(a)-1, -1, -1):
#         print(a[char], end=' ')
#
#
# reve('chandana')

# def count_(s, count = 0):
#     for char in s:
#         count += 1
#     return count
#
#
# print(count_('chANDANA'))

# def even_index(a):
#     for i in range(len(a)):
#         if i % 2 == 0:
#             print(a[i], end=' ')
#
#
# even_index('chandana')

# def digits(s):
#     for num in s:
#         if '0' <= num <='9':       #ynum.isdigit():
#             print(num, end=' ')
#
#
# print(digits('hello123hi34'))


# def digit_count(string, count=0):
#     for num in string:
#         if '0' <= num <= '9':
#             count += 1
#     return count
#
#
# print(digit_count('hai143hello654'))

# def count_spe(s, count=0):
#     for char in s:
#         if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
#             count += 1
#     return count
#
#
# print(count_spe("hi!@lo*()"))


# def lower_upper(s, a=''):
#     for char in s:
#         if 'a'<= char <= 'z':
#             a += (chr(ord(char))-32)
#         elif 'A' <= char <='Z':
#             a += (chr(ord(char))+32)
#         else:
#             a += char
#         return a
#
#
# print(lower_upper('HaiHeLLo'))


# from itertools import zip_longest
# c = ['apple', 'brown', 'college','horse']
# p = [34, 67, 87, 34 ]
# d = {}
# for i in range(len(c)):
#     d[c[i]] = p[i]
# print(d)
# d = {key:value for key, value in zip_longest(c, p)}
# print(d)


# l = ['apple', 100, '12.4', 3+4j, '56', [2,3,4]]
# l1 = [itemh[::-1] if isinstance(item, str) else item for item in l]
# print(l1)

# pr = lambda i, j: i*j
# print(pr(2,3))


# last = lambda s: s[-1]
# print(last((1, 7, 8, 7, 6, 9)))


# palin = lambda s: s if s == s[::-1] else f"{s} is not palindrome"
# print(palin("mad"))


# evens = lambda n: f"{n} is even" if n%2 == 0 else f"{n} is odd"
# print(evens(11))


list_ = ['hai', 'mom', 'dad','apple', 'ox']
# palin = lambda s: f"{s} is palindrome" if s == s[::-1] else f"{s} is not a palindrome"
# res = map(palin, list_)
# print(list(res))

# def vowel(word):
#     if word[0] in 'aeiouAEIOU':
#         return word
#
#
# res = filter(vowel, list_)
# print(list(res))


names = ['lotus-flower', 'lilly-flower', 'cat-animal', 'dog-animal']
# from collections import defaultdict
# dd = defaultdict(list)
# d = {}
# for char in names:
#      a = char.split("-")
#      if a not in d:
#          d[a[1]] += [a[0]]
#     else:
#         d[a[1]] += [a[0]]
# print(d)
# d = {}
# for i in names:
#     a = i.split("-")
#     if a[1] not in d:
#         d[a[1]] = [a[0]]
#     else:
#         d[a[1]] += [a[0]]
# print(d)


# def even(start, end):
#     li = []
#     for i in range(start, end):
#         if i % 2 == 0:
#             li.append(i)
#     return li
#
#
# print(even(1, 51))


#def prime_(end, start=2):
#     l = []
#     for n in range(start, end+1):
#         if n>1:
#             for i in range(2,n):
#                 if n % i == 0:
#                     break
#             else:
#                 l.append(n)
#     return l
#
#
# p = prime_(start=1, end=20)
# print(p)


# a = 0
# b = 1
# i = 0
# while i < 10:
#     print(a, end=" ")
#     c = a+b
#     a = b
#     b = c
#     i += 1


# def fib(n, a=0, b=1, i=0):
#     while i<n:
#         #print(a, end=" ")
#         c = a+b
#         a = b
#         b = c
#         i += 1
#     print(a, end=" ")
#fib(10)


# def int_data(*args):
#     for i in args:
#         if isinstance(i, int):
#             print(i, end=' ')
#
#
# int_data(2, 3.4, 5+6j, 4, 'hai')


# def tail(sequence, n):
#     return sequence[-n:]
#
# print(tail("hello", 2))
# print(tail("hello", 4))


# def is_perfect_sqaure(num):
#     sq = int(num ** 0.5)
#     if sq ** 2 == num:
#         return True
#     return False
#
# print(is_perfect_sqaure(5))


# def prime_(num):
#     if num>1:
#         for i in range(2,num):
#             if num % i == 0:
#                 print('not prime')
#                 break
#             else:
#                 print('prime')
#
# prime_(6)


# def is_prime(end, start=2):
#     l = []
#     for n in range(start,end+1):
#         if n>1:
#             for i in range(2,n):
#                 if n % i == 0:
#                     # print("not prime")
#                     break
#             else:
#                 l.append(n)
#     return l
# p = is_prime(start=1, end=20)
# print(p)


# def squares(n):
#     i = 0
#     l = []
#     while i <= n:
#         sq = int(i ** 0.5)
#         if sq * sq == i:
#             l.append(i)
#         i += 1
#
#     return l
#print(squares(10))


def is_prime(num):
    if num >1:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not prime"
        return f"{num} is a prime"

#print(is_prime(5))
# print(is_prime(10)


# def is_fibo(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is a fibonacci number"
#         c = a + b
#         a = b
#         b = c
#     return f"{num} is not a fibonacci number"
# print(is_fibo(7))


# l = [10, 20, 30, 40, 50, 4, 5, 6, 7]
# n = int(input("enter n:"))
# for i in range(n):
#     for j in range(len(l)-1,0,-1):
#         t = l[j-1]
#         l[j-1] = l[j]
#         l[j] = t
#     print(l)













