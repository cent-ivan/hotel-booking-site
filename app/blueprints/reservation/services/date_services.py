from datetime import datetime

def today() -> str:
    date = datetime.now().strftime('%m-%d-%Y')
    return date

def next_day():
    today = datetime.today().strftime('%m-%d-%Y')
    #divide the date
    todaySplit = today.split('-')
    month = int(todaySplit[0])
    day = int(todaySplit[1])
    year = int(todaySplit[2])
    
    def is_leap(year) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False
    
    months = {
              1: {"name": "January", "days": 31},
              2: {"name": "February", "days": is_leap(year) if 29 else 28},
              3: {"name": "March", "days": 31},
              4: {"name": "April", "days": 30},
              5: {"name": "May", "days": 31},
              6: {"name": "June", "days": 30},
              7: {"name": "July", "days": 31},
              8: {"name": "August", "days": 31},
              9: {"name": "September", "days": 30},
              10: {"name": "October", "days": 31},
              11: {"name": "November", "days": 30},
              12: {"name": "December", "days": 31}
    }
    
    #new years eve case
    if day == 31 and month == 12:
      year += 1
     
    if day == months[month]['days']:
        month += 1
        day = 1
    else:
        day += 1
    
    formattedDate = f"{str(month).rjust(2,'0')}-{str(day).rjust(2,'0')}-{year}"   
    return formattedDate