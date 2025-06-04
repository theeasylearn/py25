# if statement-
length = int(input("Enter the length "))
width = int(input("Enter the width "))
if length <0:
    length = -length
if width <0:
    width = -width
area = length* width
print("The area of the rectangle is", area)
