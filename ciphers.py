import random

def caeserCipher(text:str, key:int):
    key=int(key)
    result = ""
    print(len(text))
    # transverse the plain text
    for i in range(len(text)):
        
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result
 
def vernamCipher(encrypt:bool,text:str, key=0):
    if encrypt == True:
        key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(text)))
        ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(text, key))
    else:
        ciphertext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))

        return ciphertext
 
def decrypt(ciphertext, key):
    decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))