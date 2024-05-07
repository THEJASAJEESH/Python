a={'name':'theja','email':'thejasajeeshice@gmail.com','phone number':'8590930913'}
print(a)

#length
print(len(a))

#index
b=a['name']
print(b)

#to fetch details-get function
c=a.get('email')
print(c)

#update new values
a['name']='hello'
print(a)

#to add new values
a['age']=21
print(a)

#used copy function-to copy values
d=a.copy()
print(d)

#pop function-remove values
a.pop('name')
print(a)

#clear function-to empty the set
a.clear()
print(a)
