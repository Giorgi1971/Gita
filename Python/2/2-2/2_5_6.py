txt = input('Write txt for uncript ')
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

crpt = ''

for ch in txt:
    if ch.upper().isalpha():
        ordch = ord(ch)
        if ordch > 64 and ordch < 90:
            if ordch+num > 90:
                nord = num-(90-ordch) + 64
                ch = chr(nord)
                crpt += ch
            else:
                crpt += chr(ord(ch)+num)
        else:
            if ordch+num > 122:
                nord = num-(122-ordch) + 96
                ch = chr(nord)
                crpt += ch
            else:
                crpt += chr(ord(ch)+num)
    else:
        crpt += ch

print(crpt)
