from tkinter import *
window = Tk()
window.title("Opening Page")
window.geometry('718x400')

lbl1 = Label(window, text = "Please rate the condition of the tool on a scale from 0 (poor), to 5 (average), to 10 (perfect).")
lbl1.grid(column=300, row=0)

lblcom = Label(window, text = " ")
lblcom.grid(column=300, row=70)

def clicked():
    lblcom.configure(text = "We are sorry for your experience. Please consult the professor.")
rad1 = Radiobutton(window, text = '0', value = 1, command = clicked)
rad1.grid(column = 100, row = 30)

def clicked():
    lblcom.configure(text = "Please consult the professor to elaborate about what could have been improved.")
rad2 = Radiobutton(window, text = '5', value = 2, command = clicked)
rad2.grid(column = 100, row = 40)

def clicked():
    lblcom.configure(text = "Awesome!")
rad3 = Radiobutton(window, text = '10', value = 3, command = clicked)
rad3.grid(column = 100, row = 50)


#put stuff about rating the tool performance





