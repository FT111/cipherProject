from tkinter import *
from elements import *



class cipherInterface:
    def __init__(self, master) -> None:
        
        master.configure(bg='gray10')
        master.title('Encrypter')
        master.option_add('*Font', 'helvetica 20')
        master.option_add('*Backgound', bgPrim)
        master.option_add('*Label.Font', 'helvetica 14')
        master.geometry('800x800+0+0')

        topFrame = Frame(master, bg=bgSec)
        topFrame.pack(side='top',fill='x')
        text(topFrame,'left','h1','Encrypter')

        primaryFrame = Frame(master, bg=bgPrim)
        primaryFrame.pack(side='left', fill='x')

        textFrame = Frame(primaryFrame, bg=bgSec)
        textFrame.pack(side='left',fill='y')

        inputVar = StringVar(master)
        inputVar.set('')
        inputTextBox = textEntry(textFrame, 'left', inputVar)
        



def main():
    root=Tk()
    app=cipherInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
