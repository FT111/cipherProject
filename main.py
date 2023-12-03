from tkinter import *
from elements import tkElements
from ciphers import *
from tkinter import ttk
from functions import cipherFunctions

class cipherInterface:
    def __init__(self, master) -> None:
        
        theme = ttk.Style(master)
        theme.theme_use('clam')

        fgPrim = '#fdfdfd'
        fgSec = '#69becf'
        bg1 = 'gray20'
        bg2 = 'gray25'
        bg3 = 'gray30'
        bgPrim = 'gray10'
        bgSec = 'gray15'

        Elements = tkElements(fgPrim, fgSec, bgPrim, bgSec, bg1, bg2, bg3)
        Functions = cipherFunctions()
        
        self.Cipher = IntVar(master) # Stores cipher currently in use, controlled by radio buttons
        self.Cipher.set(0)
        outputVar = StringVar(master)
        inputVar = StringVar(master)
        keyVar = StringVar(master)

        self.nonKeyCiphers = [1]
        self.radioButtonList = []

        master.configure(bg=bgPrim) # Window configuration
        master.title('Encrypter')
        master.option_add('*Font', 'helvetica 20')
        master.option_add('*Backgound', bgPrim)
        master.geometry('715x360+0+0')

        topFrame = Frame(master, bg=bgSec) # Initialises the title bar
        topFrame.pack(side='top',fill='x')
        Elements.text(topFrame,'left','h1','Encrypter')

        primaryFrame = Frame(master, bg=bgPrim) # Initialises the container for the main frames
        primaryFrame.pack(side='left', fill=BOTH, expand=1)
        primaryFrame.subFrames = []

        for bg in [bg3, bg2, bg1]:
            primaryFrame.subFrames.append(Elements.subFrame(primaryFrame, bg, 'left')) # Initialises the main, user interactable frames

        Elements.text(primaryFrame.subFrames[0], 'top', 'h3', 'Plain Text Input', 0, 10)
        inputTextBox = Elements.textEntry(primaryFrame.subFrames[0], 'top','p', inputVar) # Shown always
        keyText = Elements.text(primaryFrame.subFrames[0], 'top', 'h3', 'Key Input', 0, 0)
        keyTextBox = Elements.textEntry(primaryFrame.subFrames[0], 'top','p', keyVar) # Shown conditionally
        
        outputBox = Elements.textOutput(primaryFrame.subFrames[2], 'top','h3', outputVar)

        for count, cipher in enumerate(CipherList,0): # Uses iteration to initialise a radio button for each cipher in the 'CipherList' list
            print(count)
            print(self.Cipher.get())
            self.radioButtonList.append(Elements.radio(primaryFrame.subFrames[1], 'top', var=self.Cipher, val=count, content=cipher, radioFunc=lambda: cipherFunctions.keyVisibility(self.Cipher,self.nonKeyCiphers,{keyText:0,keyTextBox:10})))
    

def main():
    root=Tk()
    app=cipherInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
