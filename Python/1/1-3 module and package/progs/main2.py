from sys import path
path.append('D:\\ubu\\GITA\Python\\1-3 module and package\\packages')

for p in path:
    print(p)

from extra.iota import funI
print('---')
print(funI())

