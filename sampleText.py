'''
Clark May
September 11 2020
Sample Text Project
'''

from tkinter import *
import tkinter.scrolledtext as st
from tkinter import filedialog
master = Tk()
master.title("Files")
master.geometry("800x500")  # Width x Height
master.configure(background='white')

def readFile():
    # Opening file
    file1 = open(master.filename)
    print("Using for loop")
    input_string = ""
    for line in file1:
        input_string += line
        # Closing files
    print(input_string)
    file1.close()
    sample_text(input_string)

def writeFile():
    newText = code_Text.get('1.0', 'end-1c')
    fileToWrite = open(master.filenamesave, "w")
    fileToWrite.writelines(newText)
    fileToWrite.close()

def sample_text(text_preview):
    #Label(master, text="Text Box", anchor="w", bg="Black", fg="White", font=('Helvetica', '12')).grid(row=1, column = 1)
    global code_Text
    code_Text = st.ScrolledText(master, bg='white', relief=GROOVE, font='TkFixedFont')
    code_Text.insert(INSERT, text_preview)
    #code_Text.grid(row =2, column =3)
    code_Text.place(x=100, y=5, width=300, height=300)

def openfile():
    # *** open file ***
    master.filename = filedialog.askopenfilename(initialdir="read_text/", title="Select file", filetypes=(
    ("txt files", "*.txt"), ("all files", "*.*")))
    print ("opening file at  " +str(master.filename))

def savefile():
    master.filenamesave = filedialog.asksaveasfilename(initialdir="read_text/", title="Select file", filetypes=(
    ("txt files", "*.txt"), ("all files", "*.*"))) #removed ("py files", "*.py")
    print("saving file to " + master.filenamesave)

def submenu():
    # ***main menue***
    menu =Menu(master)
    master.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="open file", command=openfile)
    subMenu.add_command(label="save file", command=savefile)
    #subMenu.add_command(label="save file", command=save_textbox)
    #subMenu.add_separator()

submenu()
#buttons
Button(master, text='Read', command=readFile, bg="Black", fg="White", activebackground="deep sky blue").place(x=0, y=5, width=40, height=20)
Button(master, text='Write', command=writeFile, bg="Black", fg="White", activebackground="deep sky blue").place(x=45, y=5, width=40, height=20)

master.mainloop()