from tkinter import *
from elements import tkElements
from functions import cipherFunctions
import ciphers

class cipherInterface:
    def __init__(self, master) -> None:

        fgPrim = '#fdfdfd'
        fgSec = '#69becf'
        bg1 = '#626570'
        bg2 = '#282828'
        bg3 = '#2e2e2e'
        bgPrim = 'gray10'
        bgSec = 'gray15'

        self.Cipher = IntVar(master) # Stores cipher currently in use, controlled by radio buttons
        self.Cipher.set(0)
        self.outputVar = StringVar(master)
        self.inputVar = StringVar(master)
        self.keyVar = StringVar(master)
        
        self.nonKeyCiphers = []
        self.radioButtonList = []

        Elements = tkElements('Helvetica',fgPrim, fgSec, bgPrim, bgSec, bg1, bg2, bg3)

        master.configure(bg=bgPrim) # Window configuration
        master.title('Encrypter')
        master.option_add('*Backgound', bgPrim)
        master.geometry('746x360')

        #
        # Top bar. Contains title text and encryption buttons
        #
        topFrame = Frame(master, bg=bgSec) # Initialises the title bar
        topFrame.pack(side='top',fill='x')
        Elements.text(topFrame,'left','h1','Encrypter')

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

        Functions = cipherFunctions(self.nonKeyCiphers, self.CipherList)

        encryptButton = Elements.button(topFrame, 'right', 'Encrypt','h2',lambda:Functions.encrypt(self.Cipher.get(),outputBox))
        decryptButton = Elements.button(topFrame, 'right', 'Decrypt','h2',lambda:Functions.decrypt(self.Cipher.get(),outputBox))

        for count, cipher in enumerate(self.CipherList,0): # Uses iteration to initialise a radio button for each cipher in the 'CipherList' list
            self.radioButtonList.append(Elements.radio(primaryFrame.subFrames[1], 'top', var=self.Cipher, val=count, content=cipher, radioFunc=lambda: Functions.keyVisibility(master,self.Cipher,{keyText:0,keyTextBox:10})))
    

def main():
    root=Tk()
    app=cipherInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
