# i_am = 'I\"m'
# print(i_am)

# # Example 1

# word = 'by'
# print(len(word))

# multiline = '''Line #1
# Line #2'''

# print(len(multiline))

# str1 = 'a'
# str2 = 'b'

# print(str1 + str1)
# print(str2 + str1)
# print(5 * 'a')
# print('b' * 4)


# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))

print(chr(ord('x')) == 'x')

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)



# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))


# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))
#  ['a','b'...]
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
print('abcabc'.count("bc"))
