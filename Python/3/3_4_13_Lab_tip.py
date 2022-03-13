class WeekDayError(Exception):
    pass


class Weeker:
    __weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__ind = self.__weekdays.index(day)
        except:
            raise WeekDayError

    def __str__(self):
        return self.__weekdays[self.__ind]

    def add_days(self, n):
        self.__ind = (self.__ind + n)% 7

    def subtract_days(self, n):
        self.__ind = (self.__ind - n) % 7


weekday = Weeker('Mon')
print(weekday.__dict__)
print(Weeker.__dict__)

try:
    print(weekday)
    weekday.add_days(1)
    print(weekday)
    weekday.subtract_days(1)
    print(weekday)

    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
