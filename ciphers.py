
def caeserCipher(text:str, key:str):
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