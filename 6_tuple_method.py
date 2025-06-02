t1 =('the',123,12.3,'easy',True,123,'easylearn')
t2 =(123,'easylearn')

# count(item) #count specified item in tuple 
print(t1.count('easylear'))  # return 0 because value in not in tuple
print(t1.count(123))
# index(item) #return index of specified item generate KeyError if item not found and program will stop
# print(t1.index('easylear'))  # return error 'x not in tuple' because value in not in tuple
print(t1.index(123))

