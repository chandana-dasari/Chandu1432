import pickle
#a = 'hello'
with open('example.pkl','rb') as file:
    c = pickle.load(file)
    print(c)


