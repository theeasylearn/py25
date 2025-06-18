import random as r
def getotp(size =6):
    if size== 8:
        return str(r.randint(10,99)) + str(r.randint(10,99)) + str(r.randint(10,99)) + str(r.randint(10,99))
    elif size == 6:
        return str(r.randint(10,99)) + str(r.randint(10,99)) + str(r.randint(10,99))
    elif size == 4:
        return str(r.randint(10,99)) + str(r.randint(10,99))
    elif size == 2:
        return str(r.randint(10,99))
    else:
        return 0

