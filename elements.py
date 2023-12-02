from tkinter import *


fgPrim = '#fdfdfd'
fgSec = '#69becf'

bg1 = 'gray20'
bg2 = 'gray25'
bg3 = 'gray30'

bgPrim = 'gray10'
bgSec = 'gray15'

textSizes = {'h1':'30','h2':'20','h3':'15'}

def subFrame(master, frameBg, frameSide):
    frame = Frame(master, bg=frameBg)
    frame.pack(side=frameSide,fill=BOTH,expand=1)
    return frame

def text(frame, textSide:str, type:str, content:str, expandText=0,padX=10,padY=10):
    label = Label(frame,fg=fgPrim,bg=frame['background'])
    label.config(text=content,font=(f'helvetica {textSizes.get(type)} bold'))
    label.pack(side=textSide,padx=padX,pady=padY,expand=expandText)

    return label

def textEntry(frame, entrySide:str, var, entryState=NORMAL):
    entry = Entry(frame, font='helvetica 14', textvariable=var, bg=frame['background'], fg=fgPrim, state=entryState)
    entry.pack(side=entrySide,padx=10,pady=10,fill=BOTH, expand=1)

    return entry

def radio(frame, radioSide:str, var, val, content:str):
    radio = Radiobutton(frame, bg=frame['background'],fg=fgPrim,selectcolor=frame['background'], activebackground=frame['background'],activeforeground=fgSec, value=val, variable=var, text=content)
    radio.pack(side=radioSide,padx=10,pady=10,fill='y')

    return radio