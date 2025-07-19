from datetime import datetime

class DateServices:
    @staticmethod
    def calculate_total_nights(checkin, checkout) -> int:
        #convert into dattime
        checkin_date = datetime.strptime(checkin,'%Y-%m-%d')
        checkout_date = datetime.strptime(checkout,'%Y-%m-%d')

        nights = checkout_date - checkin_date
        
        return nights.days

    @staticmethod
    def today() -> str:
        date = datetime.now().strftime('%Y-%m-%d')
        return date

    @staticmethod
    def next_day():
        today = datetime.today().strftime('%Y-%m-%d')
        #divide the date
        todaySplit = today.split('-')
        year = int(todaySplit[0])
        month = int(todaySplit[1])
        day = int(todaySplit[2])
        
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
        
        formattedDate = f"{year}-{str(month).rjust(2,'0')}-{str(day).rjust(2,'0')}"   
        return formattedDate