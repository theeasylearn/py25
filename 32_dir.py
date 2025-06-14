import datetime
import math 
import sys 
def showMethods(module):
    list = dir(module)
    print("----------------------------------------------------------------")
    print("method in math module",module)
    for item in list:
        print(item)

showMethods(datetime)
showMethods(math)
showMethods(sys)