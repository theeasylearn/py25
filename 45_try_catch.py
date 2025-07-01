try:
    n = int(input("enter the number "))
    if n< 0:
        n = 0- n
    qube = n *n *n
    print(f'qube is = {qube}')
except ValueError:
    print("entered number is invalid")