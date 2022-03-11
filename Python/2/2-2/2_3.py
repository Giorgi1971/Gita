# print('[' + 'Beta'.center(2) + ']')
# print('[' + 'Beta'.center(4) + ']')
# print('[' + 'Beta'.center(6) + ']')

# print('[' + 'gamma'.center(20, '*') + ']')

# t = "zeta"
# print(t.endswith("a"))
# print(t.endswith("A"))
# print(t.endswith("et"))
# print(t.endswith("eta"))

# # Demonstrating the find() method:
# print("Eta".find("ta"))
# print("Eta".find("mma"))

# # იპოვის 2-ის შემდეგ
# print('kappa'.find('a', 2))

# # ვპოულობ რამდენჯერაც არის 'the' ტექსტში
# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)
#     # ----------------------------------------------

# print('--------------------')
# # მახულობს თუ ყველა არის რიცხვი არ ალფავიტის ასო.
# t = 'Sixf lambdas'
# print(t.isalnum())

# t = 'ΑβΓფარდაδ'
# print(t.isalnum())

# t = '20E1'
# print(t.isalnum())

# # მხოლოდ ასოები
# # Example 1: Demonstrating the isapha() method:
# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # მხოლოდ ციფრები
# # Example 2: Demonstrating the isdigit() method:
# print('2018'.isdigit())
# print("Year2019".isdigit())


# # Example 1: Demonstrating the islower() method:
# print("Moooo".islower())
# print('moooo'.islower())

# # Example 2: Demonstrating the isspace() method:
# print(' \n '.isspace())
# print("    ".isspace())
# print("mooo mooo mooo".isspace(), 'პპპპ')

# # Example 3: Demonstrating the isupper() method:
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

# # Demonstrating the lower() method:
# print("SiGmA=60".lower())

# # Demonstrating the lstrip() method:
# print("[" + " tau ".lstrip() + "]")

# print("www.cisco.com".lstrip("w."))

# print("pythoninstitute.org".lstrip(".org"))

# # Demonstrating the replace() method:
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))

# # Demonstrating the rfind() method:
# print(len("tau tau tau"))
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau tau".rfind("ta", 3, 9))
# print("tau tau tau".rfind("ta", 3, 10))


# # igivewa rac strip mxolod uknida mxridan,  მარჯვნიდან
# # Demonstrating the rstrip() method:
# print("[" + " upsilon ".rstrip() + "]")
# print("cisco.com".rstrip(".com"))

# # Demonstrating the split() method:
# print("phi       chi\npsi".split())

# # Demonstrating the startswith() method:
# print("omega".startswith("meg"))
# print("omega".startswith("om"))

# print()

# # Demonstrating the strip() method:
# print("[" + "   aleph   ".strip() + "]")


# # Demonstrating the swapcase() method:
# print("I know that I know nothing.".swapcase())

# print()

# # Demonstrating the title() method:
# print("I know that I know nothing. Part 1.".title())

# print()

# # Demonstrating the upper() method:
# print("I know that I know nothing. Part 2.".upper())

strng = "To be or not to be, that is the question"
def mysplit(strng):
    ls =[]
    strng = strng.strip()
    if strng.isspace() or strng == '':
        return ls
    else:
        st =0
        fnd = strng.find(' ')

        while fnd != -1:
            ls.append(strng[st:fnd])
            st = fnd+1
            fnd = strng.find(' ', fnd+1)

        # ls.pop()
        ls.append(strng[st:len(strng)])
    return ls


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

