from datetime import datetime

def getAge(birthDate):
    day, mother, year = birthDate.split('/')
    curretYear, cuurentMonth, currentDay = datetime.today().strftime('%Y-%m-%d').split('-')

    year =+ year
    print(year)


getAge("03/08/1997")