
word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start)
	print(pos)
	if pos < 0:
		found = False
		break
	strn = strn[:pos] + strn[pos+1:]
	print(strn)
if found:
	print("Yes")
else:
	print("No")
