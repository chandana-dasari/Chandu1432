# from functools import singledispatch
# @singledispatch
# def add(a, b):
#     print("Base function add")
# @add.register(int)
# def _(a, b):
#     print("calling int")
#     return a+b
# @add.register(float)
# def _(a, b):
#     print("calling float")
#     return a+b
# a = add(4,6)
# print(a)
# a1 = add(5.4, 5)
# print(a1)



from multipledispatch import dispatch
@dispatch(int, int)
def add(a, b):
    print("int and int")
    return a + b
@dispatch(int, float)
def add(a, b):
    print("int and float")
    return a + b
@dispatch(list, str)
def concatanate(a, b):
    a.append(b)
    return a

a = add(4, 3.6)
print(a)



