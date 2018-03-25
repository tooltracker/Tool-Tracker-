from tkinter import *
window = Tk()
window.title("Opening Page")
window.geometry('718x400')

lbl1 = Label(window, text = "This ID is not being recognized as valid. Please press the button and try again.")
lbl1.grid(column=300, row=0)

btn2 = Button(window, text = "Return to previous page")
btn2.grid(column=300, row=600)
