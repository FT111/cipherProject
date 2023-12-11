from tkinter import *

class cipherFunctions:
    def __init__(self, nonKeys, cipherList) -> None:
        self.nonKeys = nonKeys
        self.cipherList = cipherList

    def setOutput(self,placeDel,placeIns,output, content):
        output.delete(placeDel,END)
        output.insert(placeIns,content)


    def keyVisibility(self,master,cipher, widgets):
        print(f'{master.winfo_width()}x{master.winfo_height()}')
        if cipher.get() in self.nonKeys:
            for widget in widgets:
                widget.pack_forget()
        else:
            for widget in widgets:
                widget.pack(side='top',padx=widgets.get(widget),pady=widgets.get(widget), expand=widgets.get(widget),fill=BOTH)
    
    def encrypt(self, cipher,output):
        for count, cipherFunc in enumerate(self.cipherList.items(),0):
            if count == cipher: 
                encryptedOutput = cipherFunc[1]()
                self.setOutput('1.0','end-1c',output, encryptedOutput)

    def decrypt(self, cipher,output):
        for count, cipherFunc in enumerate(self.cipherList.items(),0):
            if count == cipher: 
                decryptedOutput = cipherFunc[1](False)
                self.setOutput('1.0','end-1c',output, decryptedOutput)

