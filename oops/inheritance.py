# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def demo(self):
#         print(self.a + self.b)
# class B(A):
#     def demo(self):
#         print(self.a - self.b)
#         super().demo()



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         se# b = B(4, 8)
#          lf.transactions = []
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Deposited amount is {amount}")
#     def withdraw(self, amount):
#         if self.balance <
#
#
# b = BankAccount('chandu')
# print(b.balance)

# class Sample:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print(self.a + self.b)
#
# s = Sample(3,5)

# class Dad:
#     lname = 'singh'
#     def __init__(self,fname,mname):
#         self.fname = fname
#         self.mname = mname
#     def get_(self):
#         print(self.fname, self.mname, Dad.lname)
# class Mom(Dad):
#     def __init__(self, fname, mname, f_name, m_name):
#         self.f_name = f_name
#         self.m_name = m_name
#         super().__init__(fname, mname)
#     def disp(self):
#         print(self.f_name, self.m_name, Dad.lname)
#         super().get_()
# class Child(Dad, Mom):
#     def __init__(self,fname, mname, f_name, m_name, fi_name, mi_name):
#         self.fi_name = fi_name
#         self.mi_name = mi_name
#         super().__init__(fname, mname, f_name, m_name)
#     def display(self):
#         print(self.fname, self.mname, Dad.lname)
#         super().disp()

# class Parent:
#     lname = 'roy'
#     # def __init__(self, lname):
#     #     self.lname = lname
#     def disp(self):
#         return f"lastname is {Parent.lname}"
# class Dad(Parent):
#     def __init__(self, fname, mname):
#         self.fname = fname
#         self.mname = mname
#
#     def get_(self):
#         #super().disp()
#         print(self.fname, self.mname, Parent.lname)
#         #super().disp()
#
# d = Parent()
# print(d.disp())
# d1 = Dad('sree','kanth')
# d1.get_()
#


#s = "abcdddbdaefgabcdji:abcdcdedbag"
# import re
# a = re.findall(r"abcd", s)
# sum = 0
# for i in a:
#     #print(i)
#     sum += 1
# print(sum)
#count = 0
# s = "abcdddbdaefgabcdji:abcdcdedbag"
# string = 'abcd'
# x = ''
# for i in s:
#     count = 0
#     x += i
#     if len(x) == 4 and x == 'abcd':
#         count += 1
# print(count)
#
# #print(x)
# #
# i = 0
# while i < = len(s):
def compression(string):
    alist = list(string)
    master = []
    n = len(alist)
    for i in range(n):
        if alist[i] == alist[i-1]:
            master[-1] += alist[i]
        else:
            master += alist[i]
    newstring = ''
    for i in master:
        newstring += i[0] + str(len(i))
    if len(newstring) > n:
        return string
    return newstring
string = 'aabbdeeccc'
print(compression(string))
