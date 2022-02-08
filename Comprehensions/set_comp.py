'''s = {i ** 2  for i in range(1, 11)}
print(s)
'''
'''
s = {20,34,'hai',(1, 2, 3)}
res = {item for item in enumerate(s)}
print(res)

res1 = {(item, s[item]) for item in range(len(s))}
print(res1)
'''


# files = ('Amazon', 'flipkart', 'walmart', 'gmail', 'yahoo')
# res ={(item,len(item)) for item in files}
# print(res)
#
# d = {'a': 1,'b': 2,'c': 3,'d':4}
# list_ = list(d.items())
# dict_ = {item: index for index, item in enumerate(list_)}
# print(dict_)
#to check the iterable has even num of elements
# l = 'hai helo what are you'
# l1 = l.split()
# print(l1)
# set_ = {word: len(word) if len(word) % 2 == 0 else word for word in l1}
# print(set_)

# a = [1, 2.3, 'apple', 0]
# b = all(a)
# c = any(a)
# print(b)
# print(c)

# a = [1, 2, 3]
# b = a
# if b is not a:
#     print(b)
# else:
#     print(*a)
#

# string = 'hai helo'
# s1 = ''
# for  index, item in enumerate(string):
#     s1 = item + s1
# print(s1)

#print(string[::-1])

l = ['hai', 'world', 'hello','program']
# #l1=[]

# for i in range(len(l)):
# i = l[0]
# j= l[1]
# i, j = j, i
# #print(i, j, l)
# l.insert(0,i)
# l.insert(1,j)
# print(l)

#     #l[i], l[i+1] = l[i+1], l[i]
#
#
#      #l[i+1] = l[i]
# print(l)

val = []
# if val:
#     print("non default")
# else:
#     print("default")

# s = ['hai','HeLlo']
# #a = str(s)
# b=''
# for i in s:
#     for j in s[0]:
#         if 'a'<=j<='z':
#             b+=chr(ord(j)-32)
#         elif 'A'<=j<='Z':
#             b+=chr(ord(j)+32)
# print(list(b))

#a = [1,3,4]
#a = a[::-1]
#print(a)
#l =[5,1,2,3]
#l1 = list(reversed(l))
#print(l1)appl
#print(l)

# files = ['youtube.txt', 'amaxon.pdf', 'apple.xls']
# for i in files:
#     a = i.split(".")
#     #print(a)
#     if len(a[0]) % 2 !=0:
#         print(a[0])
#
# for num in [3,5,6,8,9,7]:
#     for i in range(2,num):
#         if num % i ==0:
#             break
#     else:
#         print(num)

s = ['python', 'hyderabad', 'hai']
# key = 'hello'
# print(s.remove(key))
#
# for ele in s:
#      if ele == key:
#         s.remove(key)
#         #break
        #print(s)
# key = 'hai'
# a = [s.index(0) for i in s]
# print(a)
# #print(s)


# l = ['apple','banana','apple']
# # l1 = [l.index(item) for item in l if item in l]
# # print(l1)
# for i in l:
#     for j in i:

files = ['apple.txt','yahoo.pdf']
d = {}
for file in files:
    a = file.split(".")
    #for item in a:
    d[a[1]] = a[0]
print(d)


