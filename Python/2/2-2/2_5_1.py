txt = input('Write txt for uncript ')
plain = ''

for ch in txt:
    if ch.upper().isalpha():
        if ch == 'A':
            ch = 'Z'
        plain += chr(ord(ch)-1)
    else:
        plain += ch

print(plain)
