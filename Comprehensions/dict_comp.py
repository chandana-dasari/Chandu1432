# sen = 'hai everyone hello world'
# list_ = sen.split()
# d = {}
# for word in list_:
#     d[word] = len(word)
# print(d)
#
# dict_ = {word: len(word) for word in list_}
# print(dict_)

# string = 'hello world'
# d = {}
#
# for char in string:
#
#     d[char] = string.count(char)
# print(d)
#
# dict_ = {char: string.count(char)for char in string}
#print(dict_)
# sen = 'python is a programming language, it is a easy language'
# a = sen.split()
# d = {}
# for word in a:
#     if len(word) % 2 ==0:
#         d[word] = a.count(word)
# print(d)
#
# dict_ = {word: a.count(word) for word in a if len(word) % 2 ==0}
# print(dict_)

#sent = 'hai every one how are you'
#list_ = sent.split()
#d = {}
# for word in range(len(list_)):
#     if len(list_[word]) % 2 != 0:
#         d[word] = list_[word[::-1]]
#     else:
#         d[word] = list_[word]
# print(d)

# dict_ = {word: len(word) for word in list_ if word[0] in 'aeiouAEIOU'}
# print(dict_)

# l = ['hai', 100, 5+4j,  'banana', [1,2,3], (3,5,6)]
# dict_ = {index: item if isinstance(item, str) else item[::-1] for index,item in enumerate(l)}
# print(dict_)

#d = {'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5}
# res = {}
# for key, value in d.items():
#     res[value] = key
# print(res)
#
# dict_ = {value: key for key, value in d.items()}
# print(dict_)
#
# d2 = {d[key]:key for key in d}
# print(d2)

# s = 'hello world'
# dict_ = {char: ord(char) for char in s}
# print(dict_)

# d = {'a': [1, 2, 3], 'b': [1, 2], 'c': [1, 3, 5, 7, 6]}
# a = sorted(d.items(), key=lambda item: len(item[-1]))
# print(dict(a))


# k = ['a', 'b', 'c', 'd']
# v = [2500, 5000, 2000, 1000]
# d = dict([(k[0],v[0]), (k[1], v[1]), (k[2], v[2]), (k[3], v[3])])
# print(d)
# a = sorted(d.items(), key=lambda item: (item[-1]), reverse=True)
# print(dict(a))

names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
# print(dd)
print("=============")
d = {}
for index, item in enumerate(names):
    if item not in d:
        d[item] = [index]
    else:
        d[item] += [index]
print(d)
























