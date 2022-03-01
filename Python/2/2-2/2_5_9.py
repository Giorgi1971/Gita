# import datetime
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%Y%m%d"))
# print('Input date in this Format!')

def birt_date():
    bdate = input('Enter Birth Date: ')
    while int(bdate) >= 10:    
        total = 0
        for i in str(bdate):
            total += int(i)
        bdate = total
    return total

if __name__ == '__main__':
    print(birt_date())
