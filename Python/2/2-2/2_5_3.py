def sumt():
    strs = input('Enter number with spaces ')
    stn = strs.split()
    total = 0
    try:
        for num in stn:
            total += float(num)
        print('Total is ', total)
    except:
        print(num," is not correct number")


sumt()