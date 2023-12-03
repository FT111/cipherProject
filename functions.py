from tkinter import *
from ciphers import *

class cipherFunctions:
    def __init__(self, nonKeys) -> None:
        self.nonKeys = nonKeys

    def keyVisibility(self,master,cipher, widgets):
        print(cipher.get())
        print(f'{master.winfo_width()}x{master.winfo_height()}')
        if cipher.get() in self.nonKeys:
            for widget in widgets:
                print('debug1')
                widget.pack_forget()
        else:
            for widget in widgets:
                print('debug2')
                widget.pack(side='top',padx=widgets.get(widget),pady=widgets.get(widget), expand=widgets.get(widget),fill=BOTH)
    
    def encrypt(self, cipher, input, key):
        pass