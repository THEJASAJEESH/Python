list1=['orange','apple',1,2]
print(list1)

# to find length
print(len(list1)) 

# index value
print(list1[0])
print(list1[-1])

lista=['apple','mango',3,1]
listb=['carrot',1,5,9]
listc=lista+listb
print(listc)
print(lista+listb)

list1[0]='pineapple'
print(list1)

# to add new values-append methord
list1.append('hello')
print(list1)

# insert methord
list1.insert(0,'hi')
print(list1)

# extend method
new=[8,9,7]
list1.extend(new)
print(list1)

#remove values
list1.remove(8)
print(list1)

#slicing method
list2=[1,2,3,4,5,6]
del list2[1:4]
print(list2)

list3=[4,5,6,7,1]
print(list3[2:3]+list3[4:])

# clear function
list3.clear()
print(list3)
del list3
print(list3)
