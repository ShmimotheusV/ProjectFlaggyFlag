from tkinter import *
from tkinter import ttk
from random import randint
from PIL import Image
import time


root=Tk()
boel=False
URL= r"C:\Users\timvd\Mijn Documenten_\ProjectLanden\Afbeelding"+"\\"
lijstlang=[["België",URL+"be.png"],["Frankrijk",URL+"fr.png"],["Nederland",URL+"nl.png"],["Zuid-Afrika",URL+"za.png"],["Luxemburg",URL+"lux.png"],["Barbados",URL+"bar.png"]]
lijstkort=[["Frankrijk",URL+"fr.png"]]
lijst=lijstlang
iii=0
skipBool=False

def wachtFunctie(str):
	global skipBool
	skipBool=False

#FUNCTIES
def printtext():
    global e
    string = e.get() 
    print(string) 

def doNothing():
    print("Nix! ")

def doNothing2():
    print("okokIwont!!2 ")

def doNothing3():
    print("okokIwont!!3 ")


def close_window():
    root.destroy()

def onclick(event=None):
    s=entry_1.get()
    print(s)
    entry_1.delete(0, 'end')
    global iii
    if s==lijst[iii][0]:
    	tekstbarlabel.config(text="Proficiat het is je gelukt!")
    	lijst.remove(lijst[iii])
    	if len(lijst) !=0:
    		iii=randint(0, len(lijst)-1)
    		photon=PhotoImage(file= lijst[iii][1])
    		labelfoto.configure(image=photon)
    		labelfoto.image = photon
    	else:
    		photon=PhotoImage(file=URL+"tisgebeurd.png" )
    		labelfoto.configure(image=photon)
    		labelfoto.image = photon
    		entry_1.destroy()
    		label_1.destroy()
    		c.destroy()
    		button.destroy()
    		status.destroy()
    		label_1beter=Label(root,text="Proficiat, U hebt alle vlaggen juist!!", fg="black", font=(None, 15))
    		label_1beter.grid(row=1,column=0)
    else:
    	tekstbarlabel.config(text="Bijna juist, het echte land was: "+lijst[iii][0]+"\n druk 'k' om door te gaan of wacht")
    	tellerr=1;
    	root.unbind("<Return>")
    	root.bind('k',wachtFunctie)
    	root.update()
    	global skipBool
    	skipBool=True
    	while(tellerr<20 and skipBool):
    		time.sleep(0.2)
    		tellerr+=1
    		root.update()
    	root.bind('<Return>', onclick)
    	root.unbind('k')
    	entry_1.delete(0, 'end')
    	tekstbarlabel.config(text="Bijna juist, het echte land was: "+lijst[iii][0])
    	if len(lijst)!=1:
    		huidigeiii=iii
    		iii=randint(0, len(lijst)-1)
    		if huidigeiii==iii:
    			iii=iii-1
    		photon=PhotoImage(file= lijst[iii][1])
    		labelfoto.configure(image=photon)
    		labelfoto.image = photon


#NODELOOS MENU
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="newpfoject...",command=doNothing)
submenu.add_command(label="new...",command=doNothing2)
submenu.add_separator()
submenu.add_command(label="Exit",command=doNothing3)
editmenu=Menu(menu)
menu.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="redu", command=doNothing2)
frame=Frame()


#Algemeen
root.title("ProjectLanden")
root.geometry("1000x800")
#CANVAS

photo=PhotoImage(file= lijst[iii][1])
canvas=Canvas(root,width=400,height=200)

labelfoto=Label(root,image=photo)
labelfoto.grid(row=0,column=0,columnspan=3)

label_1=Label(root,text="Antwoord")

entry_1=Entry(root)

label_1.grid(row=1,column=0)
entry_1.grid(row=1,column=1)


root.bind('<Return>', onclick)

button = Button(root, text="antwoord verzenden (of druk enter)", command=onclick)
button.grid(columnspan=2)
c=Checkbutton(root,text="Case Sensitive (doesn't work)")
c.grid(columnspan=2)

#frame = Frame(root)

button2 = Button(root)
button2['text'] ="Exit"
button2['command'] = close_window
button2.grid(row=2,column=3)

entry_1.focus_set()

#STATUSBAR

status = Label(root,text="Veel succes!", bd=1,relief=SUNKEN,anchor=W)
status.grid(row=5)

#Tekstbar
tekstbarlabel=Label(root,text="Veel succes")
tekstbarlabel.grid(row=0,column=4)




root.mainloop()