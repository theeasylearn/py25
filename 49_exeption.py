# try:
#     a=int(input("enter a : "))
#     b=int(input("enter b : "))
    
# except Exception as e:
#     print(e)
    
# else:
#     print(a+b)
    
# finally:
#     print("good bye....")

try:
    age = int(input("enter your age : "))
    if age>=18:
        print("you are eligible for voting.....")
        
    else:
        raise("invalid age!!!")
    
except ValueError:
    print("enter your age!!!")
    
except :
    print("below 18 years !!!")