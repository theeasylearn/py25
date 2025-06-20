import datetime

CurrentDateTime = datetime.datetime.now()
print(CurrentDateTime)

CurrentDate = datetime.date.today()
print(CurrentDate)

indianFormatDate = str(CurrentDate.day) + "-" + str(CurrentDate.month) + "-" + str(CurrentDate.year)
print(indianFormatDate)

usFormatDate = str(CurrentDate.month) + "-" + str(CurrentDate.day) + "-" + str(CurrentDate.year)
print(usFormatDate)

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

anotherFormat = week[CurrentDate.weekday()] + " " + str(CurrentDate.day) + "-" + str(CurrentDate.month) + "-" + str(CurrentDate.year)
print(anotherFormat)
