from tkinter import *


class tkElements:
    def __init__(self, font:str, fgPrimary, fgSecondary, bgPrimary, bgSecondary, Bg1, Bg2, Bg3) -> None:
        
        self.font = font

        self.fgPrim = fgPrimary
        self.fgSec = fgSecondary

        self.bg1 = Bg1
        self.bg2 = Bg2
        self.bg3 = Bg3

        self.bgPrim = bgPrimary
        self.bgSec = bgSecondary

        self.textSizes = {'h1':'30','h2':'20','h3':'15','p':'11'} # Text size translation for ease of use and standardisation

    def subFrame(self, master, frameBg:str, frameSide):
        frame = Frame(master, bg=frameBg)
        frame.pack(side=frameSide,fill=BOTH,expand=1)
        return frame

    def text(self, frame, textSide:str, type:str, content:str, expandText=0,padX=10,padY=10):
        label = Label(frame,fg=self.fgPrim,bg=frame['background'])
        label.config(text=content,font=(f'{self.font}',f'{self.textSizes.get(type)}', 'bold'))
        label.pack(side=textSide,padx=padX,pady=padY,expand=expandText)

        return label

    def textOutput(self, frame, entrySide:str, type:str, var):
        entry = Text(frame, font=(f'{self.font}',f'{self.textSizes.get(type)}'),fg='white', bg=frame['background'], relief=FLAT)
        entry.pack(side=entrySide,padx=10,pady=10,fill=BOTH, expand=1)

        return entry
    
    def textEntry(self, frame, entrySide:str, type:str, var):
        entry = Entry(frame, font=(f'{self.font}',f'{self.textSizes.get(type)}'), textvariable=var,bg=frame['background'], fg=self.fgPrim, width=2, highlightbackground=self.fgSec)
        entry.pack(side=entrySide,padx=10,pady=10, expand=1,fill=BOTH)

        return entry

    def button(self, frame, buttonSide:str,content:str,type:str, buttonCommand, buttonExpand=0, padding=10):
        button = Button(frame, font=(f'{self.font}',f'{self.textSizes.get(type)}', 'bold'), command=buttonCommand,bg=self.bg1,activebackground=self.fgSec, fg=self.fgPrim, text=content,highlightbackground=self.fgSec, relief=FLAT)
        button.pack(side=buttonSide,padx=padding,pady=padding, expand=buttonExpand,fill=BOTH)

        return button

    def radio(self, frame, radioSide:str, var, val, content:str,radioFunc=None):
        radio = Radiobutton(frame, font=(f'{self.font}','20'), bg=frame['background'],command=radioFunc,fg=self.fgPrim,selectcolor=frame['background'], activebackground=frame['background'],activeforeground=self.fgSec, value=val, variable=var, text=content)
        radio.pack(side=radioSide,padx=10,pady=10,fill='y')

        return radio
    