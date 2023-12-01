from tkinter import *


fgPrim = '#fdfdfd'
fgSec = '#69becf'

bgPrim = 'gray10'
bgSec = 'gray15'

textSizes = {'h1':'30','h2':'20','h3':'15'}


def text(frame, textSide:str, type:str, content:str):
    label = Label(frame,fg=fgPrim,bg=frame['background'])
    label.config(text=content,font=(f'helvetica {textSizes.get(type)} bold'))
    label.pack(side=textSide,padx=10,pady=10)

    return label

def textEntry(frame, entrySide:str, var):
    entry = Entry(frame, font='helvetica 14', textvariable=var, bg=bgSec, fg=fgPrim)
    entry.pack(side=entrySide,padx=10,pady=10)


    return entry