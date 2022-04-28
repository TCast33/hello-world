#Python program to implement a simple ceaser cipher

import sys

shift = int(sys.argv[1]) % 26
text = input()
textlen = len(text)
encrypted = ""
b=0
p=0

for e in range(0,textlen):
    charnew = ord(text[e])
    if charnew  > 64 and charnew < 91:
        charnew -= 65
        charnew = charnew + shift
        charnew = charnew % 26
        encrypted += chr(charnew + 65)
        b+=1
    elif charnew > 96 and charnew < 123:
        charnew -= 97
        charnew = charnew + shift
        charnew = charnew % 26
        encrypted += chr(charnew + 65)
        b+=1

    if b == 5 and p != 10:
        encrypted += " "
        b=0
        p+=1
    elif p==10:
        encrypted += "\n"
        p=0

print(encrypted)
