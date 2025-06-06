s ="asdsfm fdgdkms"
len(s) # default function
# user define function
def square(number): # with perameater 
    s = number * number
    # return s  # with return statement
    print("Square is =",s)

number = int(input("Enter your Number"))
ans = square(number)
# print("Square is =",ans)

def nsquare(x=2, y = 2): #here x is required and y is optional
    return (x*x + 2*x*y + y*y)
result = nsquare(3)  # 3*3 +2*3*2 +2*2
print("result is = ",result)
print("result is =",nsquare(2,3))
print("result is =",nsquare())  #nsquare() missing 1 required positional argument: 'x'
print("result is =",nsquare(y=2,x=3))

