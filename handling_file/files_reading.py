#path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"


# with open(path) as file:
#     for line_no, line in enumerate(file, start = 1):
#         print(line_no, line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         #count = 0
#         words = line.split()
#         for i in words:
#             count += 1
#     print(count)

# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         space = line.count(' ')
#         count = count + space
#     print(count)

#path = r"F:\pythonprograms\chandufile.txt"
# with open(path) as file:
#     for line in file:
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         #print(word)
#         for word in words:
#             if word[0] in 'aeiouAEIOU':
#                 count += 1
#     print(count)

# d = {}
# with open(path) as file:
#     #count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word not in d:
#                 d[word] = 1
#             else:
#                  d[word] += 1
#     print(d)

# from collections import defaultdict
# dd = defaultdict(int)
# path = r"F:\pythonprograms\chandufile.txt"
# with open(path) as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             # if word not in dd:
#             dd[word] += 1
#             # else:
#             #     dd[word] = words.count(word)
#     print(dd)


#path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\access-log.txt"
# with open(path) as file:
#     a = []
#     for line in file:
#         words = line.split()
#         a.append(words[0])
#
#         # for word in words:
#         #     a.append(word[0])
#     print(a)

# from collections import defaultdict, Counter
# dd = defaultdict(int)
# with open(path) as file:
#     #d = {}
#     for line in file:
#         if line.strip():
#             word = line.split()
#             #if word[0] not in d:
#         dd[word[0]] += 1
#             # else:
#             #     d[word[0]] += 1
    #print(dd)


# n = int(input("enter n:"))
# with open(path) as file:
#     for line_no, line in enumerate(file,start=1):
#         if line_no == n:
#             print(line)

# from itertools import islice
# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = list(islice(file, count-n, count))
#     print(res)

#with open("file1.txt","r") as file:

# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\football.txt"
# with open(path, encoding="UTF-8") as file:
#      for line in file:
#          if line.strip():
#             list_ = line.split("\t")
#             print(list_[1], end=' ')


# from collections import defaultdict
# dd = defaultdict(int)
# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.log"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             dd[list_[2]] += 1
#     print(dd)
#
#from collections import Counter
path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split()
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#     print(d)

with open(path) as file:
    for line in file:
        if line.strip():
            print(len(line), end=" ")












