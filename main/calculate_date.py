from datetime import datetime

def getAge(birthDate):
    day, month, year = birthDate.split('/')
    currentYear, currentMonth, currentDay = datetime.today().strftime('%Y-%m-%d').split('-')
    whatYear = int(currentYear) - int(year)

    if(currentMonth < month or currentMonth == month and currentDay < day):
        whatYear = whatYear - 1

    return whatYear < 0 or whatYear

print(getAge("05/11/1997"))