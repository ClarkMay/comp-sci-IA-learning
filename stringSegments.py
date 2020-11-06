'''
Clark May II
25 September 2020
2 Dimensional Arrays
Text Formatting
Reading & Writing Text Documents
'''
'''
Things To Do:
- Edit Table 
- Dropdown GUI Menu
- Save Edits (Save & Save As)
'''
from tkinter import *
from tkinter import filedialog
entries = []
class Table:
#We Can Use To Draw & Refresh The Table. Try To Redraw At The Same Time That We Save The File
    def __init__(self, root):
        #code for creating table
        #nested for loops that build the table
        for i in range(rows):
            for j in range(cols):
                    self.e = Entry(root, width=20, fg='blue',
                                   font=('Arial', 16, 'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, arr[i][j])

    def setData(self):
        print(arr)
        for i in range(rows):
            for j in range(cols):
                self.e = Entry(root, width=20, fg='blue',
                            font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, arr[i][j])
                entries.append(self.e) #this is the solution (Store entries I create into an Array)
            print(self.e)

    def getData(self):
        index = 0
        for i in range(rows):
            for j in range(cols):
                #print(entries)
                arr[i][j] = entries[index].get()
                index = index + 1
        print(arr)

def testRead():
    Table.getData(root)

def readCsv(filepath):
    # Opening file
    file1 = open(filepath)
    input_string = ""
    #-1 So That We Start At 0
    counter = -1
    for line in file1:
        input_string += line
        counter += 1
        line = line.strip('\n')
        line = line.split(',')
        size = len(line)
        for i in range(size):
            arr[counter][i] = line[i]

def csvLength(filename):
    file1 = open(filename)
    lineNumbers = 0
    for line in file1:
        lineNumbers += 1
    arrayBuilder(lineNumbers)
    return lineNumbers

def writeToFile(savefile):
    Table.getData(root)
    fileToSaveTo = open(savefile, 'w')
    for i in range(rows):
        if i > 0:
            fileToSaveTo.writelines("\n")
        for j in range(cols):
            if j < cols - 1:
                fileToSaveTo.write(arr[i][j] + ",")
            else:
                fileToSaveTo.write(arr[i][j])
    fileToSaveTo.close()

def arrayBuilder(lineNumbers):
    global arr, rows, cols
    #Defining The Size Of The Array
    rows, cols = (lineNumbers, 5)
    #Creating The Array
    arr = [["" for i in range(cols)] for j in range(rows)]
    return arr, rows, cols

rows = 0
cols = 0
# create root window
root = Tk()
#Draws the Table
Table(root)

#Use Tkinter Frame To Display the Table On
#Also Include A Scrollbar
#Get Each Text Box & Save It To A New CSV (Enable Editing)

def openfile():
    # *** open file ***
    root.filename = filedialog.askopenfilename(initialdir="read_text/", title="Select file", filetypes=(
        ("csv files", "*.csv"), ("txt files", "*.txt"), ("all files", "*.*")))
    print ("opening file at  " +str(root.filename))
    csvLength(root.filename)
    readCsv(root.filename)
    Table.setData(root)

def savefile():
    root.filenamesave = filedialog.asksaveasfilename(initialdir="read_text/", title="Select file", filetypes=(
    ("csv files", "*.csv"), ("all files", "*.*"))) #removed ("py files", "*.py")
    print("saving file to " + root.filenamesave)
    writeToFile(root.filenamesave)

def submenu():
    # ***main menu***
    menu = Menu(root)
    root.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="open file", command=openfile)
    subMenu.add_command(label="save file", command=savefile)
    #subMenu.add_command(label="save file", command=save_textbox)
    #subMenu.add_separator()

submenu()
Button(root, text = "testButton", command = testRead).grid(row=0, column=5)

root.mainloop()