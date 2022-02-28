import csv
path = r"C:\Users\Jagadeesh\PycharmProjects\Chandu1432\directory_file\files_directory\csv_files\covidcases.csv"

with open(path) as file:
    f_obj = csv.reader(file)
    print(list(f_obj))
    for row in f_obj:
        a += len(row)
    print(a)






