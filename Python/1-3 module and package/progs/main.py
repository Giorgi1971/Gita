from sys import path

path.append('..\\modules')

# path.append('D:\\ubu\\GITA\Python\\1-3 module and package\\modules')

for i in path:
    print (i)

import modules
__counter = 20

my_list = [i+1 for i in range(5)]

zeroes = [i for i in range(5)]
ones = [i+1 for i in range(5)]
# suml(zeroes)

modules.module.suml(my_list)
# suml(zeroes)
print(modules.module.prodl(ones),__counter)
# print(suml(zeroes))
# print(suml(zeroes))
# print(__counter)
