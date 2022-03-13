p1 = [0,0]
p2 = [1,1]
p3 = [3,4]


test_list = [p1,p2,p3]

# res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]

# print(res)


for ind, a in enumerate(test_list):
    print (ind, ' - -', a)
    for b in test_list[ind+1:]:
        print(ind, a, b)
