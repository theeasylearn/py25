import math as m

y = 0.5   # −1≤x≤1 value in between 
print("acos = ",m.acos(y)) # acos(x) Returns the arc cosine of x
print("asin = ",m.asin(y)) # asin(x) Returns the arc sine of x
print("atan = ",m.atan(y)) # atan(x) Returns the arc tangent of x
x = int(input("Enter the value of x in angle "))
print("cos = ", m.cos(x)) # cos(x) Returns the cosine of x
print("sin = ",m.sin(x)) # sin(x) Returns the sine of x
print("tan = ",m.tan(x)) # tan(x) Returns the tangent of x
d= m.degrees(y)
print("degrees = ",d) # degrees(x) Converts angle x from radians to degrees
print("radians = ",m.radians(d)) # radians(x) Converts angle x from degrees to radians
