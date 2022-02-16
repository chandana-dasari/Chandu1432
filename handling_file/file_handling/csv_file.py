import csv
path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\csv_files\employees.csv"
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row[0])


# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     for row in r_obj:
#         if row[3] > '70000':
#             print(row[3], end=' ')

# from collections import defaultdict
# d = defaultdict(list)
# with open(path) as file:
#     r_obj = csv.reader(file)
#     next(r_obj)
#     for row in r_obj:
#         if row[1]== 'male':
#             d[row[1]] += [row[0]]
#         else:
#             d[row[1]] += [row[0]]
#     print(d)

# from collections import defaultdict
# d = defaultdict(list)
# with open(path) as file:
#     r_obj = csv.reader(file)
#     next(r_obj)
#     for row in r_obj:
#         d[row[2]] += [row[0]]
#     print(d)

# path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\csv_files\test.csv"
# with open(path) as file:
#     sum = 0
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     print(header)
#     for row in r_obj:
#         sum += int(row[1])
#     print(sum)


path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\csv_files\vaccination_data.csv"
# with open(path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         #print(row)
#         print(row[5], end=' ')

# from collections import defaultdict
# with open(path) as file:
#     r_obj = csv.reader(file)
#     d = defaultdict(list)
#     header = next(r_obj)
#     for row in r_obj:
#         d[row[0]] += [row[5]]
#     print(d)

# from collections import defaultdict
# with open(path) as file:
#     r_obj = csv.DictReader(file)
#     d = defaultdict(list)
#     next(r_obj)
#     for row in r_obj:
#         if row["DATE_UPDATED"]:
#             d[row["DATE_UPDATED"]] += [(row['TOTAL_VACCINATIONS'],row['PERSONS_VACCINATED_1PLUS_DOSE'],row['COUNTRY'])]
#     print(d)
# res = sorted(d.items())
#print(res[-1])


