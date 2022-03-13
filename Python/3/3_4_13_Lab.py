class WeekDayError(Exception):
    pass
	

class Weeker:
    __weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day in self.__weekdays:
            self.__day = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.__day

    def add_days(self, n):
        dd = self.__weekdays.index(self.__day) + n
        wd = dd % 7
        tt = self.__weekdays[wd]
        return tt
        
    def subtract_days(self, n):
        ind = self.__weekdays.index(self.__day)
        sd = n % 7
        if ind >= sd:
            ind = ind - sd
        else:
            ind = 7 - sd + ind
        return self.__weekdays[ind]


try:
    weekday = Weeker('Mon')
    print(weekday)
    ad = weekday.add_days(15)
    print(ad)
    sd = weekday.subtract_days(1)
    print(sd)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
