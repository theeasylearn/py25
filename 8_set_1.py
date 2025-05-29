# this is set
s1 = {'a','b','c'}
s2 = {'a','c','e'}
print(s1)
# adding new element in set
s1.add('b')
s1.add('d')

s1.remove('b') # remove element from set
print(s1)
s1 = {'a','b','c'}
s2 = {'a','c','e'}

print(s1.intersection(s2)) # return element from both set but only unique
print(s2.intersection(s1)) # nothing can change set position 
print(s1.union(s2)) # return all element but only unique 
print(s2.union(s1)) # nothing can change set position 
print(s1.difference(s2)) # return unique from set 1
print(s2.difference(s1)) # return unique from set 2