# access mode = read(r) ,write(w),append(a)

obj = open("data.txt")
print("file opened...")

# print(obj)

# for i in obj:
#     for j in i:
#         print(j)

print(obj.read(3))
    
obj.close()