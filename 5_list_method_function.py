l1 =['the',123,12.3,'easy',True]
l2 =[123,'easylearn']

print(l1);print(l2)
l1.append('python') # add element on end
print(l1)
l1.extend(l2) # add list on last
print(l1)
l1 =['the',123,12.3,'easy',True]  # if you did not write again the operation happen on extend list l1
l2.extend(['l1',123])
print(l2)

l1 =['the',123,12.3,'easy',True,123]
# insert(position,item)  #Insert an item at the defined position  
l1.insert(3,'123')
print(l1)  
# remove(item)  #Removes given item from the list 
l1.remove('123')
print(l1)
# pop(position)  # Removes and returns an element at the given position
print(l1.pop(4))
print(l1)
# clear()  # Removes all items from the list
l2.clear()
print(l2)
# index()  # Returns the index of the first matched item
print(l1.index(12.3))
print(l1)   
# count(item)  #Returns the count of the number of items passed as an argument 
print(l1.count('the'))
l3 = [1,54,65,25,36,1,0]
l4 =['sdf','dfgfg','yytr']
# sort()  #Sort items in a list in ascending order if all items are of same type 
# print(l1.sort()) # return error because data type is not same
l3.sort()
print(l3)
print(sorted(l3))
print(sorted(l4))  
# reverse()  #Reverse the order of items in the list
l3.reverse()
print(l3)   
# copy()  #Returns a shallow copy of the list
l5 = l1.copy()
print(l5)
del l5[2] # delete element which  index is passed
# print(l1) # delete complete list if index is not passed
print(l5)
print(l1)
del l2
# print(l2)  # get error because l2 list is delete