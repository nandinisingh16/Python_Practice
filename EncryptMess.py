import random
import string 

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#encrypt
text=input("enter plain text ")
cipher=""

for l in text:
    index=chars.index(l)
    cipher+=key[index]
print("encrypted message is ")
print(cipher)

#decrypt
text=""
cipher=input("enter encrypted text ")

for l in cipher:
    index=key.index(l)
    text+=chars[index]
print("decrypted message is ")
print(text)
