while True:
    num = input('Enter number from 1 to 25: ')
    if not num.isdigit():
        print('Enter Only Digital Numbers!')
        continue
    else:
        num = int(num)
        if num < 1 or num > 25:
            print('Number must be in 1-25')
        else:
            break

print('Number is ', num)
