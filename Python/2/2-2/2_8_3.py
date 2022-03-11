# # One of these imports will fail - which one?

# try:
#     import math
#     import time
#     import abracadabra

# except:
#     print('One of your imports has failed.')


# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)

