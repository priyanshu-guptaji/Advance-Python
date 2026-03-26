from tkinter import *

root = Tk()
root.title("My First GUI")
root.geometry("400x300")
root.config(bg="pink")

root.minsize(width=300, height=200)
root.maxsize(width=500, height=400)

def myfunc():
    print("Priyanshu is genius!!!!!!!!!!!")

btn = Button(root, text="Click Me", command=myfunc)
btn.pack()

root.mainloop()