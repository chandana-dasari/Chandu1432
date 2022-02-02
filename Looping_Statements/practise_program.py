'''a = 'hello1234hai'
sum = 0
for i in a:
    if i.isdigit():
        sum += int(i)
print(sum)
'''

'''s = 'hello123'
count = 0
for char in s:
    if 'a' <= char <='z' or 'A' <= char <= 'Z':
        if char not in 'aeiouAEIOU':
            count += 1
            print(char, end=" ")
            #print()
            #count += 1
print()
print(count)
'''
'''a = 'helloo'
for index, item in enumerate(a):
    print((index, item),end=" ")
print("=============")
for char in range(len(a)):
    print((char,a[char]),end=" ")
'''
'''s = 'hello'
for i in s[::-1]:
    print(i, end=" ")
for i in reversed(s):
    print(i, end=" ")
for i in range(len(s)-1,-1,-1):
    print(s[i])
'''

s = 'hello123@#$$$%hai'
'''for char in s:
    if not char.isalnum():
        print(char, end=" ")
print()
for i in s:
    if not 
'''
char = 'l'
for item in range(len(s)):
    if s[item] == char:
        print(item)


