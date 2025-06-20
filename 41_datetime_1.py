import datetime as dt
#Get Current Date and Time
CurrentDateTime = dt.datetime.now()
print(CurrentDateTime) 
#Get Current Date
CurrentDate= dt.date.today()
print(CurrentDate) 
#let us get today year, month, day from date object
print("Current year: ", CurrentDate.year)
print("Current month: ", CurrentDate.month)
print("Current day: ", CurrentDate.day)
