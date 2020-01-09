from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
#Code for open new window
def openfile():
    root=Tk()
    root.title("Notepad")
    root.geometry("500x500")
    a=Text(root,font=("Calibri",12),height=500,width=500) #to get text from entry variable is a
    a.pack(fill=Y)
    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New",command=openfile)
    filemenu.add_command(label="Open...",command=appendfile)
    filemenu.add_command(label="Save..",command=filewrite)

    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.destroy)
    editmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu)
    help=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=help)
    help.add_command(label="Send feedback ")
    help.add_command(label="About Notepad")

    editmenu.add_command(label="Cut",command=sorrycut)
    editmenu.add_command(label="Copy",command=sorrycopy)
    editmenu.add_command(label="Paste",command=sorrypaste)
    root.config(menu=menubar)
    root.mainloop()

#                                           Code for help menu
#code for sending feed back
def feedback():
    root=Tk()
    root.geometry("200x125")
    root.resizable(width=False,height=False)
    b=Label(root,text="Enter your feedback from 1-5",fg="Black",padx=3,pady=2,borderwidth=2,relief="flat")
    b.pack(fill=X,padx=3,pady=3) 
    a=Entry(root)
    a.pack(fill=X)
    button=Button(root,text="Submit",bg="cyan",fg="black",relief="raised")
    button.pack(padx=5,pady=5)
    root.mainloop()
#code for about in tkinter
def about():
    
    tkinter.messagebox.showinfo("About","Notepad \nVersion 1.0")
#to create new text
def filewrite():
    dialog=filedialog.asksaveasfilename(initialdir="C:\Desktop",title="Save as..",filetypes=(("all files","*.*"),("jpeg files",".jpg")))
    text=a.get("1.0","end-1c")
    newfile=open(dialog,"w")
    newfile.write(text)
    newfile.close()
#to open a file and append
def appendfile():
    opendialogue=filedialog.askopenfilename(initialdir="C:\Desktop", title="Open as..",filetypes=(("all files","*.*"),("jpeg files",".jpg")),defaultextension="txt")
    text=a.get("1.0","end-1c")
    ofile=open(opendialogue,"a")
    ofile.write(text)
    ofile.close()
#Edit menu
def sorrycopy():
    tkinter.messagebox.showinfo("Sorry :(","Please use shortcut keyword Ctrl+C-Copy\nSorry for the inconvenience :(")
def sorrycut():
    tkinter.messagebox.showinfo("Sorry :(","Please use shortcut keyword Ctrl+X -Cut\nSorry for the inconvenience :(")
def sorrypaste():
    tkinter.messagebox.showinfo("Sorry :(","Please use shortcut keyword Ctrl+V -Paste\nSorry for the inconvenience :(")
root=Tk()
root.geometry("500x500")
root.title("Notepad")
a=Text(root,font=("Calibri",9),height=500,width=500)
a.pack(fill=Y)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=openfile)
filemenu.add_command(label="Open...",command=appendfile)
filemenu.add_command(label="Save..",command=filewrite)

filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="Send feedback ",command=feedback)
help.add_command(label="About Notepad",command=about)

editmenu.add_command(label="Cut",command=sorrycut)
editmenu.add_command(label="Copy",command=sorrycopy)
editmenu.add_command(label="Paste",command=sorrypaste)
root.config(menu=menubar)
root.configure(background="green")
root.mainloop()
