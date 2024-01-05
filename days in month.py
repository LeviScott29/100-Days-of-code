while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("invalid entry, can only enter integer")
while True:
    try:
        month =int(input("enter a month in number format: "))
        break
    except ValueError:
        print("invalid input. can only enter an integer")

def days_in_month(year, month):
    leap= is_leap(year)
    month=month%12
    month_days = [31, 28, 31, 30, 31, 30,  31, 31, 30, 31, 30, 31]
    days= month_days[month-1]
    if month == 2 and leap== True:
        return ("there is 29 days")
    else: return ("this month has", days), "days"
    
        
def is_leap(year):

    lpc1 = year % 4

    if lpc1 != 0:
        return False
    elif lpc1 == 0:
        lpc2 = year % 100

        if lpc2 != 0:
            return True
        elif lpc2 == 0:
            lpc3 = year % 400

            if lpc3 != 0:
                return False
            elif lpc3 == 0:
                return True
            else:
                pass
        else:
            pass
    else:
        pass

return_days= days_in_month(year, month)
print(return_days)


