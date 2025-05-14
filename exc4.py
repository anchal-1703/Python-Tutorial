"""secret code language"""
# if word contain atlest 3 charac ,remove the first letter and append it at  the end now append 3 random char at the beg and end
# else simply reverse the string
# decoding 
# if the letter contain atleast 3 word reverse it
# else remove 3 random char from start and end and place the last cha at the beg 
import random
import string
code=input("enter your code word")
if len(code)>=3:
    encode=code[1:]+code[0]
    add=''
    for i in range(3):
        a=random.choice(string.ascii_letters)
        add+=a
    print(add+encode+add)
else:
    for i in range(1,-1,-1):
        print(code[i],end='')
1