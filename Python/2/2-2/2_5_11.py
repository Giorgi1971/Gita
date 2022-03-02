def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


rows = []
for r in range(9):
    ok = False
    while not ok:
        row = input('Enter row #'+str(r+1)+': ')
        # თუ შეტანილი მონავემების სიგრძეა 9 ან ყველა არის ციფრი, მაშინ  
        ok = len(row) == 9 or row.indigit()
        if not ok:
            print("inncorrect data - 9 digits required")
        rows.append(row)
ok = True

for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

if ok:
    for r in range(0,9,3):
        for c in range(0,9,3):
            sqr = ''
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

if ok:
    print ('Yes')
else:
    print('No')