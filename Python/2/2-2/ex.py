strng = '012 45 789 1011'
st =0
fnd = strng.find(' ')
ls = []

while fnd != -1:
    print(fnd)
    ls.append(strng[st:fnd])
    st = fnd+1
    fnd = strng.find(' ', fnd+1)

# ls.pop()
ls.append(strng[st:len(strng)])


print(ls)

