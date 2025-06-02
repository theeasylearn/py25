book ={}  # empty dictionary create
print("empty dic")
print(book)
# add key with value n dictionary
book['name'] = 'python for ds'
book['price'] = 1200
book['weight'] = 12.3
print(book)
# multiple value with single key
book['ch'] =(1,2,3,4) # 
book['topic'] = ['en',2,'eco']

print(book)
book['topic'] = 'python library' # replace value with key
print(book)

b1 = book.copy()  # create copy of dictionary 
b1

print(book.items()) # print all items
print(book.keys()) # return keys as list

print(book.values()) # return values as list
print(book)
print(book.pop('weight',12.3))
print(book)
print(book.popitem())
print(book)
book.clear() # delete all element from dictionary
print(book) # return empty dictionary
del b1['topic'] # delete value where key is topic
print(b1)