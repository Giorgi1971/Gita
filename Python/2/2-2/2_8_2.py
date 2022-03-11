# # This code cannot be terminated
# # by pressing Ctrl-C.

# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     # except IndexError:
#     except KeyboardInterrupt:
#         print("Don't do that!")


# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

