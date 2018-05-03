from tkinter import *

root=Tk()
topframe=Frame(root)

topframe.pack()
botomframe=Frame(root)
botomframe.pack(side=BOTTOM)

button1=Button(topframe,text="Button 1",fg="red")
button2=Button(topframe,text="Button 2",fg="green")
button3=Button(topframe,text="Button 3",fg="brown")
button4=Button(botomframe,text="Button 4",fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


root.mainloop()
