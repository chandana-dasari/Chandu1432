#s = {'python', 'dad', 'malayalam', 'hai', 'madam'}
#for item in set_:
 #   print(item)
key = 'dad'
#s.discard(key)
#print(s)
'''for ele in s:
    if ele == key:
        s.discard(key)
        break
print(s)
'''
li = ['python', 'dad', 'malayalam', 'hai', 'madam', 'mom']
s = set()
for item in li:
    if item == item[::-1]:
        s.update({item})  #s.add(item)
print(s)


