from tkinter import *
from collections import Counter
import string, operator
import numpy as np
import matplotlib.pyplot as plt
from elements import tkElements


class cipherFunctions:
    def __init__(self, cipherList) -> None:
        self.cipherList = cipherList
        self.standardFrequency = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074}
        self.sortedFreq =  dict(sorted(self.standardFrequency.items(), key=operator.itemgetter(1)))

    def setOutput(self,placeDel,placeIns,output, content):
        output.delete(placeDel,END)
        output.insert(placeIns,content)

    def frequencyAnalysis(self, output):
        
        pltFigure, axis = plt.subplots(2, 1) # Sets a 2 graph grid in Matplotlib.

        c = Counter(output.get('1.0',END))
        axis[0].bar(*zip(*c.most_common()), color='g') # Plots the cipher's letter frequencies, in descending order.
        axis[0].set_title('Cipher Text Frequency')
        
        axis[1].bar(self.sortedFreq.keys(), self.sortedFreq.values()) # Plots the standard English letter frequencies below.
        axis[1].invert_xaxis()

        # Displays the graph
        plt.show()

    def cipherInfo(self, master, windowElements, text:list):
        subWindow = Toplevel()
        subWindow.title('Encryption Info')
        subWindow.geometry('1250x200')
        subWindow.option_add('*Backgound', windowElements.bgPrim)

        mainFrame = Frame(subWindow, bg=windowElements.bgPrim)
        mainFrame.pack(fill=BOTH,expand=1)
        subFrames = []

        for frame in range(2):
            subFrames.append(windowElements.subFrame(mainFrame,windowElements.bgPrim,'left'))
            subFrames[frame].out = windowElements.textOutput(subFrames[frame], 'top','p')
            subFrames[frame].out.insert('end-1c', text[frame])
            
                             

                

            


    
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

