try:
    n1 = int(input("Entre the value of n1 "))
    n2 = int(input("Enter the value of n2 "))
    division = n1/n2
    print(f"division is {division}")
except ValueError:
    print("invalid input Enter the numeric value only")
except ZeroDivisionError:
    print("zero is not valid")
