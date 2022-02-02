#d = {'a': 1, 'b': 2,'c': 3,'d':4, 'e':5}

'''for key in d.keys():
    print(key, end=' ')
print()

#traversing through dictionary directly
for key in d:
    print(key, end= ' ')
print()

for key in d.values():
    print(key, end= ' ')
print()
#using get()
for key in d:
    print(d.get(key), end= ' ')
print()
#using items()
for key, value in d.items():
    print(value,end= ' ')
for key, value in enumerate(d):
    print(d[value] , end= ' ')

s = 'hello world'
di = {}
#count = 0
for i in set(s):
    count = 0
    for j in s:
        if i == j:
            count += 1
    di[i] = count
print(di)

s = 'hehh'
d = {}
for char in s:
    #if char not in d:
     #   d[char] = 1
    #else:
    d[char] += 1
print(d)

s = 'python is a language, python programming is easy'
a = s.split(' ')
print(a)
d = {}
for i in a:
    count = 0
    for j in a:
        if i == j:
            count+= 1
    d[i] = count
print(d)
print("=================>")
d1 ={}
for word in a:
    d1[word] = a.count(word)
print(d1)
print("==============>")
d2 = {}

for word in a:
    if word not in d2:
        d2[word] = 1
    else:
        d2[word] += 1
print(d2)
print("===============>")
from collections import defaultdict
s = 'python is a language, python programming is easy'
a = s.split(' ')
dd = defaultdict(int)
#print(dd)
for word in a:
    dd[word] = dd[word] + 1
print(dd)



from collections import defaultdict
dd = defaultdict(int)
s = 'python is a language, python programming is easy'

list_ = s.split(" ")
for word in list_:
    if len(word) % 2 == 0:
        d[word] = len(word)
print(d)


from collections import defaultdict
dd = defaultdict(int)
s = 'python is a language, python programming is easy'
#d = {}
list_ = s.split(" ")
for word in list_:
    if word[0] in 'aeiouAEIOU':
        dd[word] = len(word)
print(dd)


s = 'python is a language, python programming is easy'
list_ = s.split(" ")
d = {}
for word in list_:
    if list_.count(word) > 1:
        pass
    else:
        d[word] = list_.count(word)
print(d)
'''
#names = ['apple', 'gmail','apple', 'gmail']
'''d = {}
for word in names:
    count = names.count(word)
    if names.count(word) > 1:
        d[word] = count
print(d)
'''
s = 'hi hello  how is your work '
'''from collections import defaultdict
dd = defaultdict(list)
a = s.split()
for word in a:
    dd[word[0]].append(word)
print(dd)

names = ['apple', 'gmail', 'google', 'apple', 'gmail', 'google']
d = {}
for word in range(len(names)):
    #print(word)
    if names[word] not in d:
        d[names[word]] = [word]
    else:
        d[names[word]] += [word]
print(d)
'''
d = {'a': 1, 'b': 2, 'c': 3}
# for


    #print(index,item)





