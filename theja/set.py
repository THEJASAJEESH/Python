a={1,2,3}
print(a)
print(len(a))
b={'good','hello world','hi'}
print(b)
print('bye' in b)

b.add('bye')
print(b)
b.update(['goodu','hkh'])
print(b)

# b.remove('the')
# print(b)
b.discard('the')
print(b)

#union
a={1,2,3}
b={4,5,6}
c=a.union(b)
print(c)
a={1,2,3}
b={2,3,4}

#intersection
c=a.intersection(b)
print(c)
a={6,7,8}
b={6,1,2}

#difference
c=b.difference(a)
print(c)

#clear
a={1,2,3}
a.clear()
print(a)
del a
print(a)



