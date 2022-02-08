# "program to get the indexes of each item in the list"
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'gmail', 'gmail']
# # from collections import defaultdict
# # dd = defaultdict(list)
# d = {}
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item].append(index)
# print(d)

# sen = 'python is a program'
# l = sen.split()
# rres = map(len, l)
# print(list(rres))

# word = 'python'
# print(list(lambda word: ord(ch)))


# def ascii_(ch):
#     return ch, ord(ch)
#
#
# res = map(ascii_, word)
# print(list(res))


# string = 'hello world'
# from collections import defaultdict
# dd = defaultdict(int)
# for char in string:
#     dd[char] = string.count(char)
# print(dd)


# sen = 'python is a programming language'
# list_ = sen.split()
# from collections import defaultdict
# dd = defaultdict(int)
# for index, item in enumerate(list_):
#     if len(item) % 2 == 0:
#         dd[index] = item
#     else:
#         dd[index] = item[::-1]

#print(dd)


files = ['apple.txt', 'amazon.pdf', 'yahoo.txt','flipkart.pdf']
# from collections import defaultdict
# dd = defaultdict(list)
# for file in files:
#     a = file.split('.')
#     dd[a[1]] += a[0]
#
# print(dd)

# s = 'programming'
# from collections import defaultdict
# dd = defaultdict(int)
# for char in s:
#     if s.count(char) > 1:
#         dd[char] = s.count(char)
#
# print(dd)

#a = ['a', 'b']


# def func(word):
#     return word


# res = list(map(list, a))
# print(res)


#n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# from collections import defaultdict
# dd = defaultdict(list)
# for num in n:
#     if num % 2 == 0:
#         dd[0] += [num]
#     else:
#         dd[1] += [num]
# print(dd)

# d = {}
# even_list = []
# odd_list = []
# for num in n:
#     if num % 2 ==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# d[0] = even_list
# d[1] = odd_list
# print(d)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def square_(num):
#     return num ** 2
#
#
#
# res = filter(square_,range(0, len(l)+1, 2))
# print(list(res))


# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# from collections import defaultdict
# dd = defaultdict(int)
# for item in names:
#     if names.count(item) > 1:
#         dd[item] = names.count(item)
# print(dd)


# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = {}
# for item in items:
#     fname, ext = item.split("-")
#     if ext not in d:
#         d[ext] = [fname]
#     else:
#         d[ext] += [fname]
# print(d)


# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value
# print(d)

# items = ['hai', '20', '3+4j', 'hello', '34', '85']
# k = 2
# for item in range(k):
#     l = item.pop()
#     print(l)
#     items.append(l)
# print(items)

# cities = ['Tokyo', 'Delni', 'shanghai', 'mumbai','chennai']
# population = ['34,000,000', '21,435,000', '23,456,100', '34,678,000']
# from itertools import zip_longest
# d = {k:v for k,v in zip_longest(cities,population)}
# print(d)

# l = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 8, 9, 9]
# d1 = {'0': [l[item]] for item in range(len(l)) if item % 2 == 0}
# d2 = {'1': [l[item]] for item in range(len(l)) if item % 2 != 0}
# print(d1)
# print(d2)
# for item in range(len(l)):
#     print(item)

# D = {'names': 'apple', 'ID':12345}
# d = {'names': 'apple', 'ID':23444}
# dict_ = {key: value for key, value in zip(D.keys(), d.values())}
# print(dict_)


# s = [(4, 56, 98), ('one', 'Two', 'Three')]
# for i in s:
#     print(i)
#
# d = {item1[1]: item2[0] for item1, item2 in enumerate(s)}
# print(d)

# se = 'python is a programming language'
# li = se.split()
# l = (sorted(li, key=len))
# print(l)
# print(l[-1],l[0])

# l = sorted(li, key=len)
# print((l[-1], len(l[-1]), (l[0], len(l[0])))
# #print((l[0], len(l[0])))


# li = ['python', 'java', 'ruby', 'perl']
# def mid_ch(ele):
#     return ele[len(ele)] // 2
#
# print(sorted(li, key=mid_ch))

# d = {'gmail':5, 'apple': 13, 'walmart': 1, 'flipkart': 38}
# #print(sorted(d, key=lambda item: item[-1]))
# print(sorted(d.values()))
# print(sorted(d.items(), key=lambda item: item[len(item[-1])]))

# t = [('Delhi', 32), ('Mumbai', 27)]
# print(sorted(t, key=lambda item: item[-1]))

s = 'python is a programming language and programming is very fun'
l = s.split()
d = {word:len(word) for word in l if l.count(word) == 1}
print(d)
res = sorted(d.items(), key=lambda item: item[-1])
print(res[-1])








