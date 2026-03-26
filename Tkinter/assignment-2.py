# Tkinter

from sys import maxsize
from tkinter import *
root=Tk() #used to create aplication using TK functions
root.title("My First GUI")
root.geometry("400x300") #used to set the size of the window
root.config(bg="pink") #used to set the background color of the window
root.minsize(width=300,height=200) #used to set the minimum size of the window
root.maxsize(width=500,height=400) #used to set the maximum size of the window

#1.button
def myfunc():
    print("Jai Mata Di!!")
btn=Button(root,text="Click Me",font=("Arial",8),bg="yellow",fg="brown",command=myfunc) #used to create a button
btn.pack() #used to display the button

#2.Label
lbl=Label(root,text="Giet is not  a good collage",font=("Arial",12),bg="cyan",fg="black") #used to create a label
lbl.pack() #used to display the label

var=StringVar() #used to create a variable
#3.Checkbutton

def check():
    print(var.get())
chk=Checkbutton(root,text="Check Me",variable=var,onvalue="Checked",offvalue="Unchecked") #used to create a checkbox
chk.pack() #used to display the checkbox
b= Button(root,text="Submit",command=lambda:print(var.get())) #used to create a button
root.mainloop() #used to run the application

# Input field -     entry
def submit():
    print("You entered:", entry.get()) #used to get the value from the input field      

entry=Entry(root,font=("Arial",12),bg="white",fg="black") #used to create an input field
entry.pack() #used to display the input field

b=Button(root,text="Submit",command=submit) #used to create a button
b.pack() #used to display the button

def show():
    print("You entered:", entry.get()) #used to get the value from the input field
rb1=Radiobutton(root,text="Option 1",value=1,command=show) #used to create a radio button
rb1.pack() #used to display the radio button
rb2=Radiobutton(root,text="Option 2",value=2,command=show) #used to create a radio button
rb2.pack() #used to display the radio button
rb3=Radiobutton(root,text="Option 3",value=3,command=show) #used to create a radio button
rb3.pack() #used to display the radio button







root.mainloop()