# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# from collections import deque
# n = 3
# with open(path) as f:
#     res = deque(f, n)
#     print(list(res))

# class Instance:
#     count = 0
#     def __init__(self, a):
#         self.a = a
#     def __iter__(self):
#         return iter(self.a)
#
# i = Instance([1,2,3,4,5])
# for ele in i:
#     print(ele)

#print(list(dd))


# s = 'banana'
# from collections import defaultdict
# d = defaultdict(int)
# for i in s:
#     if s.count(i) > 1:
#         d[i] += 1
#
# print(d)


# a = 'chandana'
# l = []
# for i in a[::2]:
#     l += i
# print(l)

# l = [5, 6, 7, 8, 9]
# res = lambda item: item**2
# s = [res(i) for i in l]
# print(s)
# a = 'hello'
# l = list(a)
# print(l)
# b = ''.join(l)
# print(b)
# b =''
# for i in a[::-1]:
#     b+=i
# print(b)
# a = ['h', 'e', 'l', 'l', 'o']
# b = ''

#check two strings are anagrams or not

# def anagram(s1, s2):
#     if s1.upper() == s2.upper():
#         return False
#     st1 = sorted(s1.upper())
#     st2 = sorted(s2.upper())
#     if st1 == st2:
#         return True
#     else:
#         return False
# print(anagram('ate', 'eat'))
# print(anagram('hello', 'world'))
#print(anagram('Under', 'ground'))
# l = [3, 4, 5, 6, 7]
# res = map(lambda item:item**2, [3, 4, 5, 6, 7])
# print(list(res))
# li = [res[i] for i in l]
# print(li)
# s = "This is a programming language and programming is fun"
# l = s.split()
# d = {word:len(word) for word in l if l.count(word)==1}
# print(d)
# s = sorted(d.items(), key=lambda item:item[-1])
# print(s[-1])

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# from collections import defaultdict
# d = defaultdict(int)
# for word in names:
#     d[word] += 1
# print(d)
# for key, value in d.items():
#     if value>1:
#         print(key)

# n = 5
# for i in range(1, n+1):
#     if n>1:
#         if n % i == 0:
#             print("prime")
# else:
#     print("not prime")

l = [10, 4, 5, 20, 45, 4, 2, 6]
large = 0
for num in l:
    if num > large:
        large = num
print(large)

# s = sorted(l)
# print(s[-1])



















# class Dict:
#     def __init__(self,a):
#         self.a = a
#     def __getitem__(self, item):
#         return self.a[item]
#     def __getattr__(self, name):
#         return self.a[name]

# d = Dict({'a': 1, 'b': 2})
# print(d.b)
# print(d['a'])

# c1 = Instance()
# #print(c1.count)
# c2 = Instance()
# c3 = Instance()
#print(c2.count)
#print(Instance.count)


        #print(self.count)
# from collections import defaultdict
# dd = defaultdict(int)
# def instance_count(func):
#     def wrapper(*args, **kwargs):
#         dd








# from itertools import islice
# n = 0
# a = 5
# # def random_line(n):
# with open(path) as file:
#     res = islice(file, n, a)
#     print(list(res))


#random_line(1)

# with open(path) as file:
#     for line_no, line in enumerate(file, start = 1):
#         print(line_no, line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         #count = 0
#         words = line.split()
#         for i in words:
#             count += 1
#     print(count)

# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         space = line.count(' ')
#         count = count + space
#     print(count)

#path = r"F:\pythonprograms\chandufile.txt"
# with open(path) as file:
#     for line in file:
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         #print(word)
#         for word in words:
#             if word[0] in 'aeiouAEIOU':
#                 count += 1
#     print(count)

# d = {}
# with open(path) as file:
#     #count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word not in d:
#                 d[word] = 1
#             else:
#                  d[word] += 1
#     print(d)

# from collections import defaultdict
# dd = defaultdict(int)
# path = r"F:\pythonprograms\chandufile.txt"
# with open(path) as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             # if word not in dd:
#             dd[word] += 1
#             # else:
#             #     dd[word] = words.count(word)
#     print(dd)


#path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\access-log.txt"
# with open(path) as file:
#     a = []
#     for line in file:
#         words = line.split()
#         a.append(words[0])
#
#         # for word in words:
#         #     a.append(word[0])
#     print(a)

# from collections import defaultdict, Counter
# dd = defaultdict(int)
# with open(path) as file:
#     #d = {}
#     for line in file:
#         if line.strip():
#             word = line.split()
#             #if word[0] not in d:
#         dd[word[0]] += 1
#             # else:
#             #     d[word[0]] += 1
    #print(dd)


# n = int(input("enter n:"))
# with open(path) as file:
#     for line_no, line in enumerate(file,start=1):
#         if line_no == n:
#             print(line)

# from itertools import islice
# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = list(islice(file, count-n, count))
#     print(res)

#with open("file1.txt","r") as file:

# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\football.txt"
# with open(path, encoding="UTF-8") as file:
#      for line in file:
#          if line.strip():
#             list_ = line.split("\t")
#             print(list_[1], end=' ')


# from collections import defaultdict
# dd = defaultdict(int)
# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.log"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             dd[list_[2]] += 1
#     print(dd)
#
#from collections import Counter
path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split()
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#     print(d)

# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(len(line), end=" ")

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)












