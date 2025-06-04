m = int(input("Enter the number of month "))
if m>0 and m<=12:
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print("31 days in this month")
        if m== 8:
            print("August")
    elif m==4 or m==6 or m==9 or m==11 :
        print("30 days in this month")
    else:
        print("28/29 days in this month")
else:
    print("Invalid month")