#executing function for 3 times

# def spam(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#             #print(res[::-1])
#     return wrapper
#
# def add(a, b):


import time
def outer(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            func(*args, **kwargs)
        return wrapper
    return delay

@outer(2)
def add(a, b):
    print(a + b)
add(4, 5)
@outer(5)
def exp(a, b):
    print(a * b)
exp(4, 4)





