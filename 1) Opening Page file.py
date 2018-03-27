from tkinter import *
window = Tk()
window.title("Opening Page")
window.geometry('718x400')

lbl1 = Label(window, text = "Welcome to Tool Tracker!")
lbl1.grid(column=300, row=0)

lbl2 = Label(window, text = "Please enter Student ID:")
lbl2.grid(column=300, row=100)

idlist = []

def update(number):
    #specify the length of the ID 
    if len(idlist)<6:
        #add the new number pressed into the array 
        idlist.append(number)
        print(idlist)
        ID=""
        for n in range(len(idlist)):
            ID+=str(idlist[n])
        print(ID)
        lblBlank = Label(window, text = ""+ ID)
        lblBlank.grid(column=300, row=200)

lblID = Label(window, text = print(idlist))
lblID.grid(column=300, row=200)

def clicked():
    update(1)
btn1 = Button(window, text = "1", command = clicked)
btn1.grid(column=299, row=600)

def clicked():
    update(2)
btn2 = Button(window, text = "2", command = clicked)
btn2.grid(column=300, row=600)

def clicked():
    update(3)
btn3 = Button(window, text = "3", command = clicked)
btn3.grid(column=301, row=600)

def clicked():
    update(4)
btn4 = Button(window, text = "4", command = clicked)
btn4.grid(column=299, row=700)

def clicked():
    update(5)
btn5 = Button(window, text = "5", command = clicked)
btn5.grid(column=300, row=700)

def clicked():
    update(6)
btn6 = Button(window, text = "6", command = clicked)
btn6.grid(column=301, row=700)

def clicked():
    update(7)
btn7 = Button(window, text = "7", command = clicked)
btn7.grid(column=299, row=800)

def clicked():
    update(8)
btn8 = Button(window, text = "8", command = clicked)
btn8.grid(column=300, row=800)

def clicked():
    update(9)
btn9 = Button(window, text = "9", command = clicked)
btn9.grid(column=301, row=800)

def clicked():
    update(0)
btn0 = Button(window, text = "0", command = clicked)
btn0.grid(column=300, row=900)

btnsub = Button(window, text = "Submit ID")
btnsub.grid(column=300, row=1000)
