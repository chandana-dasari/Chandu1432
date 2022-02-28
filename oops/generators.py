# def greet():
#     return 'hello'

l = [1,2,3,4,5]
def square():
    for i in l:
        yield i * i
s = square()
print(list(s))





# res = (i ** 2 for i in l)
# print(res)

#write a generator function and expression to yield length of each line in a file only if the line is not empty
path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
def func():
    # open(path) as file:
        #obj = file.read()
    file = open(path)
    for line in file:
        if line.strip():
            yield len(line)
    #file.seek(0)
    res = (len(line) for line in file if line.strip())
    #print(list(res))

f = func()
print(list(f))
# with open(path) as file:





