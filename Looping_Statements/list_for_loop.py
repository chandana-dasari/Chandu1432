li = [10,3.5,'python',(1,2,3)]
for index , item in enumerate(li):
    print(index,'-->',item)
for ele in range(len(li)):
    print("index is:",ele)
    print("element is:",li[ele])

li = [10,3.5,'python',(1,2,3)]
for item in range(len(li)-1, -1, -1):
    print(li[item])
#Using slicing
for i in li[::-1]:
    print(i)
#using range
for item in range(5, 0, -1):
    print(li[item])

li = [10, 3.5, 'python', ]
for item in reversed(li):
    print(item)

#printing alternate elements
l = [20, 'java', 4.5, (2,4,6)]
for ele in range(len(l)):
    if ele %2 == 0:
        print(l[ele], end = ' ')
print()
for ele in range(0,len(l),2):
    print(l[ele], end = ' ')
print()
for ele in l[::2]:
    print(ele, end = ' ')
print()

#odd index elements
l = [20, 'java', 4.5, (2,4,6)]
for ele in range(len(l)):
    if ele %2 != 0:
        print(l[ele], end = ' ')
print()
for ele in range(1,len(l),2):
    print(l[ele], end = ' ')
print()
for ele in l[1:len(l):2]:
    print(ele, end = ' ')
print()



l = ['python', 10, 3.2, 'selenium', 'java', True]
for ele in l:
    if isinstance(ele, (int, float, complex)):
        print(ele, end= ' ')
print()
for ele in l:
    if isinstance(ele, int):
        print(ele, end= ' ')
print()
'''

#l = ['hai', 'hello', 'world']
#for ele in l:
 #   print((ele, len(ele)))
#print()
l = ['Node JS', 'python', 'java', 'selenium']
li = []
for item in l:
    if len(item) % 2 == 0:
        print(item)     #li += [item]    li.append(item)
    else:
        print(item[::-1])    #li.append(item[::-1])
print(li)

a = [1, 2.3, 'banana',{1,2,3}, 'hyderabad',[4,5,6]]
b = []
for i in a:
    if isinstance(i, str):
        b.append(i[::-1])
    else:
        b.append(i)
print(b)


files = ['Amazon', 'flipkart', 'walmart', 'gmail', 'yahoo']
for ele in files:
    if ele[0] in 'aeiouAEIOU':
        print(ele)

files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
ex = []
for item in files:
    a = item.split(".")
    b = a[1]
    ex += [b]       #ex.append(b)
print(ex)

for file in files:
    filename, extension= file.split(".")
    print(extension)

    #if len(file) % 2 != 0:
     #   print(file)


nums = [10,20,40,30,20,40,50]
num = 40
print(nums.index(num))
for index, item in enumerate(nums):
    if item == num:
        print(f"{num} is ")

if True:
    print("True", end=' ')
if False:
    print("False")

x = 10.0
y = (x < 100.0) and isinstance(x, float)
print(y)

print(15.0 == 34.5)
a = 'hello world'
print(if a.count(" ") > 1 "statement1" else "statement2")
a = [1,2,3]
b = ['a','b', 'c']
if a > b:
    print("a is greater")
else:
    print("b is greater")

a = 'hello'
if a.find("z"):
    print("True")
else:
    print("False")
 

for n in range(10):
    if n>1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n)

l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
for i in l:
    if i[:] == i[::-1]:
        print(i)



