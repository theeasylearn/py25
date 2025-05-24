l1 =['the',123,12.3,'easy',True]
l2 =[123,'easylearn']
print(l1);print(l2)
l1.append('python')
print(l1)
l1.extend(l2)
print(l1)
l1 =['the',123,12.3,'easy',True]  # if you did not write again the operation happen on extend list l1
l2.extend(['l1',123])
print(l2)