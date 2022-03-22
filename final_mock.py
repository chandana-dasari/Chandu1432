# words = ['look', 'into', 'my', 'eyes', 'look', 'in', 'my', 'eyes', 'look']
# from collections import Counter
# c = Counter(words)
# print(c)
# print(c.most_common())

# import re
# ele = re.findall(r'\s', 'hello how are you')
# count = 0
# for i in ele:
#     count += 1
# print(count)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0,len(a),2):
#     print(a[i:i+2])


# class Decorator(object):
#     def __init__(self, arg):
#         self.arg = arg
#     def __call__(self,cls):
#         def wrapper(*args):
#             return cls(*args)
#         return type("TestClass", (cls,), dict(newMethod=self.newMethod,classattr=self.arg))
#     def newMethod(self, value):
#         return value * 2
# @Decorator("decorated class")
# class TestClass(object):
#     def __init__(self):
#         self.name = "TestClass"
#         print("init %s", self.name)
#     def TestMethodInTestClass(self):
#         print("test method in test class")
#     def newMethod(self, value):
#         return value * 3
# t = TestClass(50)

from itertools import zip_longest
t1 = ('rose', 'red', 'green')#[('rose', 2),('red',3),('green', 4),('rose',5)
t2 = (2, 3, 4, 5, 6, 7, 8, 9, 10)
temp1 = len(t1)
temp2 = len(t2)
for i in range(temp2):
    print(t2[i], t1[i%temp1])
# # t = [[i, j] for i, j in zip_longest(t1, t2)]
# print(t)
# i = 0
# while i <= len(t2):
#     for index, item in enumerate(t):
#         if item[0] == None:
#             item.remove(None)
#             item.insert(0, t1[i])
#             i += 1
#        print(item)

            #return func(n, i+1)
#f = func(t)
        # print(item)


    # else:
    #     item.remove(None)
    #     item.insert(0, 'red')
    #     print(item)

#[(


