from tkinter import *
from ciphers import *

class cipherFunctions:
    def keyVisibility(cipher, nonKeys, widgets):
        print(cipher.get())
        if cipher.get() in nonKeys:
            for widget in widgets:
                print('debug1')
                widget.pack_forget()
        else:
            for widget in widgets:
                print('debug2')
                widget.pack(side='top',padx=widgets.get(widget),pady=widgets.get(widget), expand=widgets.get(widget),fill=BOTH)
