class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__housrs = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        if self.__housrs < 10:
            hh = '0'+ str(self.__housrs)
        else:
            hh = str(self.__housrs)
        if self.__minutes < 10:
            mm = '0'+ str(self.__minutes)
        else:
            mm = str(self.__minutes)
        if self.__seconds < 10:
            ss = '0'+ str(self.__seconds)
        else:
            ss = str(self.__seconds)
        return hh+':'+mm+':'+ss

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__housrs += 1
                if self.__housrs == 24:
                    self.__housrs = 0
        

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__housrs -= 1
                if self.__housrs == -1:
                    self.__housrs = 23
        


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
