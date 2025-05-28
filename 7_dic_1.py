# Dictionary creation with element 
d1= {
    'name' : 'D',
    'age': 26,
    'subject': 'python'
}
print(d1)
d1['name'] = "D Patel" # update element using key
print(d1)
d1['date'] = "10/02/2025" # add element with key and value 
print(d1)

del d1['age']  # delete using key
print(d1)