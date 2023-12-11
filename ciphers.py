import random, functions


class Ciphers:
    def __init__(self, keyVar, inputVar, keyBox) -> None:
        self.keyVar = keyVar
        self.inputVar = inputVar
        self.keyBox = keyBox

    def caeserCipher(self, encrypt=True):
        try:
            key=int(self.keyVar.get())
        except ValueError: # Only handles the error if the key isn't an integer.
            return 'Invalid key'

        if encrypt==False:
            key = -1*key # Changes key to negative for decryption
        
        text=self.inputVar.get()
        result = ""
        # Transverse the plain text
        for i in range(len(text)):
            
            char = text[i]
            # Encrypt uppercase characters in plain text
            
            if (char.isupper()):
                result += chr((ord(char) + key-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            elif char==' ':
                result += ' '
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result
    
    def vernamCipher(self, encrypt=True):
        text = self.inputVar.get()
        if encrypt == True:
            key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(text))) # Generates a key
            ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(text, key)) # Encryption
            functions.cipherFunctions.setOutput(self,'0','0',self.keyBox,key)
        else:
            ciphertext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, self.keyVar.get())) # Decryption

        return ciphertext
    
    def vigenereCipher(self, encrypt=True):
        key = self.keyVar.get()
        text = self.inputVar.get().upper()
        key = list(key)
        cipherText = []
        if len(text) == len(key): # Formatting key
            return(key)
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        key = "" . join(key)
        if encrypt==True: # Encryption
            for i in range(len(text)): # Each letter uses a seperate ceaser cipher
                x = (ord(text[i]) + ord(key[i])) % 26 
                x += ord('A')
                cipherText.append(chr(x))
        else:
            for i in range(len(text)):
                x = (ord(text[i]) - ord(key[i]) + 26) % 26 # Decryption
                x += ord('A')
                cipherText.append(chr(x))
        return "".join(cipherText)
    