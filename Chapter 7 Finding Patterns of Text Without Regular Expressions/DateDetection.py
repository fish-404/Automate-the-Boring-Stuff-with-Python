import re

# year range from 1000 to 2999
def __isYearValid__(yearStr : str):
    yearInt = int(yearStr)
    if yearInt < 1000 or yearInt > 2999:
        return False
    else:
        return True

def __isLeapYear__(yearStr : str):
    yearInt = int(yearStr)
    if yearInt % 100 == 0 and yearInt % 400 != 0:
        return False
    elif yearInt % 4 == 0:
        return True

# month range from 01 to 12
# if month < 10, assume it has a leading zero 
def __isMonthValid__(monthStr : str):
    monthInt = int(monthStr)
    if monthInt < 1 or monthInt > 12:
        return False
    else:
        return True

def __isValidSmallMonthDay__(dayInt : int, monthStr : str):
    smallMonthRegex = re.compile(r'[04|06|09|11]')
    if smallMonthRegex.search(monthStr) != None and dayInt <= 30:
        return True
    else:
        return False

def __isValidFebruaryDay__(dayInt : int, yearStr : str):
    if __isLeapYear__(yearStr) and dayInt <= 29:
        return True
    elif not __isLeapYear__(yearStr) and dayInt <= 28:
        return True
    else:
        return False

# date range from 01 to 31
# if day < 10, assume it has a leading zero
def __isDayValid__(dayStr, monthStr, yearStr):
    dayInt = int(dayStr)
    if (monthStr == "02") and not __isValidFebruaryDay__(dayInt, yearStr):
        return False
    elif not __isValidSmallMonthDay__(dayInt, monthStr):
        return False 
    elif dayInt > 31:
        return False
    else:
        return True 

def DateDetection(sentence : str):
    dateRegex = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
    matchObj = dateRegex.search(sentence)
    if matchObj == None:
        return False

    day = matchObj.group(1)
    month = matchObj.group(2)
    year = matchObj.group(3)

    if __isYearValid__(year) \
        and __isMonthValid__(month) \
        and __isDayValid__(day, month, year):
        return True
    else:
        return False
    

        




   

    

