'''program to remove duplicate from list'''
names = ['apple', 'ggogle', 'apple', 'yahoo', 'google']
res = []
for item in names:
    if item in names:
        pass
    else:
        names.remove(item)
print(names)

