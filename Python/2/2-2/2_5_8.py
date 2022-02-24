txt1 = input('Enter text1: ').replace(' ', '').upper()
txt2 = input('Enter text2: ').replace(' ', '').upper()
l1 = sorted(list(txt1))
l2 = sorted(list(txt2))
if l1 == l2:
    print('Yes')
else:
    print('No')