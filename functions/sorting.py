l = ['python', 'java', 'c', 'perl', 'ruby']
def last_ele(l):
    return l[-1]
#print(sorted(l, key = last_ele))

s = sorted(l, key = lambda item: item[0])
print(s)
