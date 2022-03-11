# from math import tan, radians
# angle = int(input('Enter integral angle in degrees: '))

# # We must be sure that angle != 90 + k * 180
# assert angle % 180 != 90
# print(tan(radians(angle)))

# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')

