# file = open("data.txt",'a')
# file.write("\nthis new data...")

# file.close()

# write a program that copy from one file and paste to other file
copy = input("enter file to copy : ")
paste = input("enter file to paste : ")

file1 = open(copy,'r')
data = file1.read()
print("data copied...")

file2 = open(paste,"w")
file2.write(data)
print("data pasted...")

obj = open(copy,'w')
obj.write("")




obj.close()
file1.close()
file2.close()