w1 = input('Enter first word: ')
w2 = input('Enter second word: ')


lt = []
for i in w1:
    if i in w2:
        lt.append(True)
    else:
        lt.append(False)
    
print(lt)
if False in lt:
    print('No')
else:
    print('Yes')