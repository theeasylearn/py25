# write a program that find no of character in file
# find vowels and consonents of file


name = input("enter file name : ")
file = open(name,"r")

vowel = ["a","e","i","u","o"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

vc=0
cc=0
nc=0

count = 0 
# for i in file:
#     for j in i:

for i in file.read():
        count+=1
        
        if i in vowel:
            vc+=1
            
        elif i in numbers:
            nc+=1
            
        else:
            cc+=1
    
    
print("total char of file : ",count)
print("total vowel : ",vc)
print("total consonantes : ",cc)
print("total numbers : ",nc)