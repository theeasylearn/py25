# def add():
#     return 0

# def add(a):
#     return a+a

# def add(a,b):
#     return a+b

# print(add(1))

def add(a=0,b=0):
    if a==0 and b==0:
        return 0
    
    elif (a!=0 and b==0):
        return a+a
    
    elif (a==0 and b!=0):
        return b+b
    
    elif a!=0 and b!=0:
        return a+b
    
    
print(add())
print(add(5))
print(add(5,10))