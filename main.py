from tkinter import *
from elements import tkElements
from functions import cipherFunctions
import ciphers

class cipherInterface:
    def __init__(self, master) -> None:

        fgPrim = '#fdfdfd'
        fgSec = '#69becf'
        bg1 = '#333a49'
        bg2 = '#282828'
        bg3 = '#2e2e2e'
        bgPrim = '#1a202f'
        bgSec = 'gray15'

        self.Cipher = IntVar(master) # Stores cipher currently in use, controlled by radio buttons
        self.Cipher.set(0)
        self.outputVar = StringVar(master)
        self.inputVar = StringVar(master)
        self.keyVar = StringVar(master)

        infoText = ['Symmetric encryption involves the use of one key for both encryption and decryption. The plaintext is read into an encryption algorithm along with a key. The key works with the algorithm to turn the plaintext into ciphertext, thus encrypting the original sensitive data. This works well for data that is being stored and needs to be decrypted at a later date. The use of just one key for both encryption and decryption reveals an issue, as the compromise of the key would lead to a compromise of any data the key has encrypted.', 
                    'Asymmetric encryption works with a pair of keys. The beginning of asymmetric encryption involves the creation of a pair of keys, one of which is a public key, and the other which is a private key. The public key is accessible by anyone, while the private key must be kept a secret from everyone but the creator of the key. This is because encryption occurs with the public key, while decryption occurs with the private key.']
        
        self.radioButtonList = []

        Elements = tkElements('Helvetica',fgPrim, fgSec, bgPrim, bgSec, bg1, bg2, bg3)

        master.configure(bg=bgPrim) # Window configuration
        master.title('Encrypter')
        master.option_add('*Backgound', bgPrim)
        master.geometry('723x400')

        
        #
        # Left Bar. Contains the info button and additional buttons if added
        #
        leftFrame = Frame(master, bg=bgPrim)
        leftFrame.config(width=10)
        leftFrame.pack(side='left', fill='y')
        infoButton = Elements.smallButton(leftFrame, 'top', '🛈',lambda:Functions.cipherInfo(master,Elements,infoText),0) # Places info button in the frame, uses a preset small button.

        #
        # Top bar. Contains title text and encryption buttons
        #
        topFrame = Frame(master, bg=bgSec) # Initialises the title bar
        topFrame.pack(side='top',fill='x')
        Elements.text(topFrame,'left','h1','Encrypter')

        # Info Frame

        infoFrame = Frame(master, bg=bgPrim)


        #
        # Primary Frame. Contains the main control frames that handle user input.
        #
        primaryFrame = Frame(master, bg=bgPrim) # Initialises the container for the main frames
        primaryFrame.pack(side='left', fill=BOTH, expand=1)
        primaryFrame.subFrames = []

        for bg in [bg3, bg2, bg1]:
            primaryFrame.subFrames.append(Elements.subFrame(primaryFrame, bg, 'left')) # Initialises the main, user interactable frames
    
        Elements.text(primaryFrame.subFrames[0], 'top', 'h3', 'Input Text', 0, 10)
        inputTextBox = Elements.textEntry(primaryFrame.subFrames[0], 'top','p', self.inputVar) # Shown always
        keyText = Elements.text(primaryFrame.subFrames[0], 'top', 'h3', 'Key', 0, 0)
        keyTextBox = Elements.textEntry(primaryFrame.subFrames[0], 'top','p', self.keyVar) # Shown conditionally

        Elements.text(primaryFrame.subFrames[2], 'top','h3','Output')
        outputBox = Elements.textOutput(primaryFrame.subFrames[2], 'top','p', self.outputVar)

        Ciphers = ciphers.Ciphers(self.keyVar, self.inputVar, keyTextBox)

        self.CipherList = {'Caeser Cipher': Ciphers.caeserCipher, 'Vernam Cipher': Ciphers.vernamCipher, 'Vigenére Cipher': Ciphers.vigenereCipher} # List of ciphers

        Functions = cipherFunctions(self.CipherList)

        encryptButton = Elements.button(topFrame, 'right', 'Encrypt','h2',lambda:Functions.encrypt(self.Cipher.get(),outputBox))
        decryptButton = Elements.button(topFrame, 'right', 'Decrypt','h2',lambda:Functions.decrypt(self.Cipher.get(),outputBox))
        freqButton = Elements.smallButton(leftFrame, 'top', '📊',lambda:Functions.frequencyAnalysis(outputBox),0) # Places info button in the frame, uses a preset small button.

        for count, cipher in enumerate(self.CipherList,0): # Uses iteration to initialise a radio button for each cipher in the 'CipherList' list
            self.radioButtonList.append(Elements.radio(primaryFrame.subFrames[1], 'top', var=self.Cipher, val=count, content=cipher))
    

def main():
    root=Tk()
    app=cipherInterface(root)
    root.mainloop()



if __name__ == "__main__":
    main()
