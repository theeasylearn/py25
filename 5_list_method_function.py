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

del l1[2] # delete element which  index is passed
print(l1) # delete complete list if index is not passed

del l2
# print(l2)  # get error because l2 list is delete