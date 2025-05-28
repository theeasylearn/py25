name ="it"
print(name)
print(type(name))
name1="abc"

name = "the easylearn" # change all string
print(name)
print(name[::])
print(name[1]) # only single 
print(name[0:5]) # [start:end]
print(name[0:5:2]) # [start:end:Step]
# name[0]="T"  #get error because string is inmutable 
print(name[:5]) # start index is default 0
print(name[4:]) # end index take default length of string-1

print(name)
print(name*3) # return three time string
print(name+" "+name1) #concatenate name and name1 with space