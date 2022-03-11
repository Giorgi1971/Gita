def read_int(prompt, min, max):
    x = input(prompt)
    try:
        x = int(x)
        if x < min or x > max:
            raise
    except ValueError:
        print('Error: Enter only numbers')
    except:
        print('Error: not in range')
    return x




    #
    # Write your code here.
    #


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
