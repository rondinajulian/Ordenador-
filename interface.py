from os import read
from tkinter import*

#raiz

raiz = Tk()
raiz.resizable(0,0)

miFrame = Frame(raiz,width="800",height="450")
miFrame.pack()

cuadroTexto= Entry(miFrame)
cuadroTexto.grid(row=1,column=0, padx=10,pady=10)

nombreLabel = Label(miFrame,text="Que ordenamos hoy?")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)















raiz.mainloop()
