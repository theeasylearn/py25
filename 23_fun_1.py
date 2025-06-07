# default function
s ="asdsfm fdgdkms"
len(s) 

# user define function
# with parameter with return
def square(number): # with parameter 
    s = number * number
    return s  # with return statement
# calling function
number = int(input("Enter your Number"))
ans = square(number)
print("Square is =",ans)

# without return without parameter
def greet(): # without parameter
    print("Hello, how are you?") # without return statement
    
greet() # calling function

# without parameter with return 
import datetime

def get_current_datetime():
    return datetime.datetime.now()

# Calling the function
current_time = get_current_datetime()
print("Current Date and Time:", current_time)

# with parameter without return
day =int(input("Enter the day number"))

def daycount(day):
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Invalid day number")
daycount(day)