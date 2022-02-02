#print 1 to 10
for num in range(10,1,-1):
    print(num)
#print 1 to 10
for num in range(10,1,-1):
    print(num)
#print 1 to 10
for num in range(1, 11):
    print(num)
#print 10 to 1
for num in range(10, 1, -1):
    print(num)
#print -1 to -10
for num in range(-1,-11,-1):
    print(num)
#print -10 to -1
for num in range(-10, 0):
    print(num)


# even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# traversing through strings
string = 'python'
for char in string:
    print(char , end = " ")
for item in range(len(string)):
    print(item , end = " ")
    print(string[item])


li = [1 , 2 , 3 , 'hai']
for item in li:
    print(item)
for item in range(len(li)):
    print(li[item])


tu = [1, 2, 3, 'hai']
for item in tu:
    print(item, end = " ")
for item in range(len(tu)):
    print(tu[item] , end=" ")


string = 'chandana'
for item in range(len(string)-1, -1,-1):
    print(string[item], end = " ")
print()
for char in string[::-1]:
    print(char, end = " ")
print()
for item in reversed(string):
    print(iteml, end = " ")

string = 'hello'
count = 0
for item in string:
    count += 1
print(count)


string = 'hello'
for char in range(len(string)):
    if char % 2 == 0:
        print(string[char], end = " ")
print()
for char in string[::2]:
    print(char, end = " ")

s = 'hai143 %$2345'
count = 0
for digit in s:
    if '0'<= digit <= '9':
        count+=1
print(count)



