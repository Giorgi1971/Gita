from sys import path

# path.append('..\\modules')

path.append('D:\\ubu\\GITA\Python\\1-3 module and package\\mod2')

for i in path:
    print (i)

from extra.good.best.tau import FunT

print(FunT())
