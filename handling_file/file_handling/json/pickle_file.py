# import pickle
# #a = 'hello'
# with open('example.pkl','rb') as file:
#     c = pickle.load(file)
#     print(c)

# import json
# b = 'hai'
# #path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\handling_file\file_handling\json\example.json"
# with open('display.json', 'rb') as f:
#     g = f.read()
#     o = json.loads(g)
#     print(type(o))
#     print(o)
    # j = json.dumps(b)
    # f = json.loads(j)
    # print(f)
    #print(j)
    #f.write(j)
    # print(j)
    #f.write("how are you")


# n = 153
# a = str(n)
# b = len(a)
# res = 0
# for i in a:
#     res += int(i)**b
# if res == n:
#     print("amstrong")
# else:
#     print("not amstrong")

# class Sorting:
#     def sor(self, l):
#         for i in range(len(l)):
#             for j in range(i + 1, len(l)):
#                 if l[i] > l[j]:
#                     l[i], l[j] = l[j], l[i]
#         return l
#
#         # s1 = sorted(l)
#         # print(s1)
#
# s = Sorting()
# print(s.sor([4, 3, 6, 1, 7, 5]))

# n = 'madam1'
# s = ''
# for i in n:
#     s = i + s
#     #print(s)
# if n == s:
#     print("palindrome")
# # n = 345
# sum = 0
# while n > 0:
#     a = n % 10  #5
#     sum = (sum*10) + a
#     n = n // 10
# print(sum)

class Sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sam(self):
        print(self.a+self.b)
    @classmethod
    def disp(cls, c, d):
        print(c+d)
s = Sample(4, 6)
Sample.disp(6, 2)
s.sam()

















































