name ="it"
print(name)
print(type(name))

name = "the easylearn" # change all string
print(name)
print(name[0:5]) # [start:end]
print(name[0:5:2]) # [start:end:Step]
# name[0]="T"  get error because string is inmutable 
print(name[:5]) # start index is default 0
print(name[4:]) # end index take default length of string-1
print(name[2]) # only single 
print(name)
print(name*3)
print(name+name)