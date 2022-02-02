#l = [1, 2, 3, 4, 5]
#Using list_comprehension
'''res = [(index, item) for index, item in enumerate(l)]
print(res)

#Normal method
l_ = []
for index, item in enumerate(l):
    l_.append((index, item))
print(l_)
'''

'''
l = list(range(10))
even = [i for i in l if i % 2 == 0]
odd = [i for i in l if i % 2 != 0]
'''
#l = ['python', 'node js', 'selenium', 'java',10, 10.5,True]
'''res = []
for word in l :
    if isinstance(word, str):
        res.append(word[::-1])
    else:
        res.append(word)
print(res)

l = ['python', 'node js', 'selenium', 'java','Amazon']
res = [i for i in l if i[0] in 'aeiouAEIOU']
print(res)
'''

'''l = ['python', 'node js', 'selenium', 'java','Amazon']
res = [item for item in enumerate(l)]
print(res)
print()
res1 = [(i, l[i])for i in range(len(l))]
print(res1)
'''
#Reversing the elements
'''l = ['python', 'node js', 'selenium', 'java', 'Amazon']
rev = [i for i in l[::-1]]
print(rev)
rev1 = [i for i in reversed(l)]
print(rev1)
rev2 = [l[i] for i in range(len(l)-1,-1,-1)]
print(rev2)
'''
#print alternative elements
'''l = ['python', 'selenium', [1,2], 10]
alter = [item for item in l[::2]]
print(alter)
alter1 = [l[i] for i in range(0,len(l),2)]
print(alter1)
alter2 = [l[item] for item in range(len(l)) if item % 2 == 0]
print(alter2)
'''
#integers present in a list using list comprehension
'''li = ['hai', 34, 5.5,23, True]
res = [i for i in li if isinstance(i, int)]
print(res)
'''
'''l = ['hai', 'hello', 'yummy', 'bangalore']
length = [(i, len(i)) for i in l]
print(length)
length1 = [(l[i], len(l[i])) for i in range(len(l))]
print(length1)
'''
#strings are of even length
'''l = ['hai', 'hello', 'chandana', 'yummy', 'bangalore', 'blue']
res = [word for word in l if len(word) % 2 == 0]
print(res)
'''
'''l = [1.4,  4, 3]
res = {i ** 2 for i in l}
print(res)
'''
# n = 56
# for i in range(2,n):
#     if n%i ==0:
#         print("not prime")
#         break
# else:
#     print("prime")


# str_ = 'python'
# for i in reversed(str_):
#     print(i,end=" ")
# print("======================")
# new_str = ""
# for j in range(len(str_)-1, -1, -1):
#     print(str_[j])
#     o

string = 'malayalam'
a = 'l'
for i in string:
    if i == a:
        print(string[i])
        break


