"print from 10 to 1"


# def count_(start, end):
#     if start <= end:
#         return
#     print(start, end=' ')
#     count_(start-1, end)
#
#
# count_(10, 1)


# def add_digit(num):
#     count = 0
#     for i in str(num):
#         count += int(i)
#     print(count)
#
#
# add_digit(143)


# num = 123
# sum = 0
# while num > 0:
#     last = num % 10
#


# def add_digit(num, sum = 0):
#     if num > 0:
#         last = num % 10
#         sum += last
#         num //= 10
#         return add_digit(num, sum)
#     else:
#         return sum
#
#
# print(add_digit(123))


# n = 5
# sum = 0
# i = 0
# while i < n:
#     sum += i
#     i += 1
# print(sum)


# def sum_num(n, sum = 0):
#     if n > 0:
#         sum += n
#         n -= 1
#         return sum_num(n, sum)
#     else:
#         return sum
#
# print(sum_num(4))
#
#
# print(sum_num(5))

# def fact(n, sum = 1):
#     if n>0:
#         sum *= n
#         return fact(n-1, sum)
#     return sum
#
#
# print(fact(5))



# def count_digit(n,count = 0):
#     if n > 0:
#         # last = n % 10
#         # count += 1
#         n = n//10
#         count += 1
#         return count_digit(n, count)
#     return count
#
#
# print(count_digit(75848))

# s = 'hai'
# a =''
# i =0
# while i < len(s):
#     a = s[i] + a
#     i += 1
# print(a)
#
#
# def rev_string(s, a='', i=0):
#     if i < len(s):
#         a = s[i] +a
#         return rev_string(s, a, i+1)
#     return a
#
#
# print(rev_string('hai'))

# def fibo(n):
#     if n < 0:
#         print("invalid input")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fibo(n-2)+fibo(n-1))
# n = int(input("ehter a:"))
# print("fibonacci series:", end=' ')
# for i in range(n):
#     print(fibo(i), end=' ')


# def fact(n, sum=1):
#     if n>0:
#         sum *= n
#         return fact(n-1,sum)
#     return sum
#
#
# f = fact(5)
# print(f)
#
#
#
# print(fibo(9))
#
#
# def re(string):
#      print(string)
#      return re(string[1::])
# re("hai")
#


# def prime_(n):
#      if n > 1:
#           for i in range(2, n):
#                if n % i == 0:
#                     return (n+1)
#           return n
#
# print(prime_(15))



