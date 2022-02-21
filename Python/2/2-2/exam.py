p1 = '# # #  '
p2 = '#      '
p3 = '    #  '
p4 = '#   #  '

n1 = [p3,p3,p3,p3,p3]
n2 = [p1,p3,p1,p2,p1]
n3 = [p1,p3,p1,p3,p1]
n4 = [p4,p4,p1,p3,p3]
n5 = [p1,p2,p1,p3,p1]
n6 = [p1,p2,p1,p4,p1]
n7 = [p1,p3,p3,p3,p3]
n8 = [p1,p4,p1,p4,p1]
n9 = [p1,p4,p1,p3,p1]
dicn = {1:n1,2:n2,3:n3,4:n4,5:n5,6:n6,7:n7,8:n8,9:n9}
lsm = [n1,n2,n3,n4,n5,n6,n7,n8,n9]


def draw(numb):
    for i in range(5):
        lsl = ''
        for j in str(numb):
            lsl = lsl + lsm[int(j)-1][i]
        print(lsl)

draw(987654321)