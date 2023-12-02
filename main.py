from tkinter import *
from elements import *
from ciphers import *
from tkinter import ttk

class cipherInterface:
    def __init__(self, master) -> None:
        
        theme = ttk.Style(master)
        theme.theme_use('clam')
        
        self.Cipher = IntVar(master).set(0) # Stores cipher currently in use, controlled by radio buttons
        outputVar = StringVar(master).set('')
        inputVar = StringVar(master).set('')
        keyVar = StringVar(master).set('')

        master.configure(bg=bgPrim) # Window configuration
        master.title('Encrypter')
        master.option_add('*Font', 'helvetica 20')
        master.option_add('*Backgound', bgPrim)
        master.option_add('*Label.Font', 'helvetica 14')
        master.geometry('715x360+0+0')

        topFrame = Frame(master, bg=bgSec) # Initialises the title bar
        topFrame.pack(side='top',fill='x')
        text(topFrame,'left','h1','Encrypter')

        primaryFrame = Frame(master, bg=bgPrim) # Initialises the container for the main frames
        primaryFrame.pack(side='left', fill=BOTH, expand=1)
        primaryFrame.subFrames = []

        for bg in [bg3, bg2, bg1]:
            primaryFrame.subFrames.append(subFrame(primaryFrame, bg, 'left')) # Initialises the main, user interactable frames

        text(primaryFrame.subFrames[0], 'top', 'h3', 'Plain Text Input', 0, 10)
        inputTextBox = textEntry(primaryFrame.subFrames[0], 'top', inputVar) # Shown always
        keyText = text(primaryFrame.subFrames[0], 'top', 'h3', 'Key Input', 0, 0)
        keyTextBox = textEntry(primaryFrame.subFrames[0], 'top', keyVar) # Shown conditionally
        
        outputBox = textEntry(primaryFrame.subFrames[2], 'top', outputVar, DISABLED)


        radioButtons = []
        for count, cipher in enumerate(CipherList,0): # Uses iteration to initialise a radio button for each cipher in the 'CipherList' list
            radioButtons.append(radio(primaryFrame.subFrames[1], 'top', var=self.Cipher, val=count, content=cipher))


def main():
    root=Tk()
    app=cipherInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
