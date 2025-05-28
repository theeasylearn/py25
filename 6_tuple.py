t1 =('the',123,12.3,'easy',True,123,'easylearn')
t2 =(123,'easylearn')
print(t1);print(t2) # print tuple in different line
print(t1[4]) # return 5th element
print(t1[1:3]) # return 2nd & 3rd element
print(t1[:3]) # default index take 0 if not given
print(t1[2:5]) # [start_index : end_index]
print(t1[2:]) # default index take size-1 if not given
print(t1+t2) # concatenate both tuple
t3=print(t1+t2)
print(t3)
print(t2*3) # return three time tuple
print(t1[-1]) # return last element of tuple
print(t1[-2]) # return second last element of tuple
print(t1) 
print(t1[-5:]) # return from last 5th element to last element
print(t1[:5])  # return first five element