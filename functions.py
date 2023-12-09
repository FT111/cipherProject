from tkinter import *

class cipherFunctions:
    def __init__(self, nonKeys, cipherList) -> None:
        self.nonKeys = nonKeys
        self.cipherList = cipherList

    def keyVisibility(self,master,cipher, widgets):
        print(f'{master.winfo_width()}x{master.winfo_height()}')
        if cipher.get() in self.nonKeys:
            for widget in widgets:
                widget.pack_forget()
        else:
            for widget in widgets:
                widget.pack(side='top',padx=widgets.get(widget),pady=widgets.get(widget), expand=widgets.get(widget),fill=BOTH)
    
    def encrypt(self, cipher,input,output,key=0):
        for count, cipherFunc in enumerate(self.cipherList.items(),0):
            if count == cipher: 
                if key == '':
                    key = 0
                encryptedOutput = cipherFunc[1](input,key)
                print(encryptedOutput)
                output.delete(1.0,END)
                output.insert('end-1c',encryptedOutput)

        