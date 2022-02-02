'''
number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is not an even number")

char_ = '98'
if 'a' <= char_ <= 'z':
    print(f"{char_} is in lowercase")
else:
    if 'A' <= char_ <= 'Z':
        print(f"{char_} is in uppercase")
    else:
        print(f"{char_} is not an alphabet")

char_ = 'r'
if 'a' <= char_ <= 'z':
    print(f"{char_} is in lowercase")
if 'A' <= char_ <= 'Z':
    print(f"{char_} is in uppercase")
else:
    print(f"{char_} is not an alphabet")

iterable = 'hello'
if len(iterable) > 0:
    print("Iterable is not empty")
else:
    print("Iterable is empty")

iterable = 'hello'
if iterable:
    print("Iterable is not empty")
else:
    print("Iterable is empty")

value = 'chandu'
if value:
    print("value is not a default vaue")
else:
    print("it is a default value")

letter = 'F'
if letter.islower() or letter.isupper():
    #print(chr(ord(letter)-32))
    #print(letter.upper())
    print(letter.swapcase())
#elif letter.isupper():
 #   print(letter.lower())
#else:
 #   print(f"{letter} is not a character")

string = 'akshara'
if string in 'aeiou':
    print('starts with vowel')
else:
    print("not strt with vowel")

string = 'akshara'
if string[-1] in 'aeiouAEIOU':
    print("yes")
else:
    print("no")

string = 'Mom'
a = string.lower()
if a == a[::-1]:
    print(f"{string} is a palindrome ")
else:
    print(f"{sring} is Not a palindrome")

number = 1441
num = str(number)
if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")


li = {1,34,56}
b = str(li)
if len(li) % 2 == 0:
    print(f"{li} has even elements")
else:
    print(f"{li} does not have even elements")


num = 6543
a = str(num)
if int(a[0]) % 2 == 0:
    print("even")
else:
    print("odd")


Greatest of three numbers
a = 10      #int(input("Enter a :"))
b = 20       #int(input("Enter b :"))
c = 10      #int(input("Enter c :"))
#print(max("print of greatest number", Greatest))

if a > b and a > c:
    print("a is greater")
elif b>c:
    print("b is greater")
#elif c>a and c>b:
 #   print(f"{c} is greater")
else:
    print("c is greater")


#Check Character is a vowel or not
char = 'b'
if char in 'aeiouAEIOU':
    print('Given character is a vowel')
    li = [(char, ord(char))]
    print(dict(li))
else:
    print('Given character is a consonant')

'''