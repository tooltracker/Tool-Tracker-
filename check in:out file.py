from tkinter import *
window = Tk()
window.title("Check In/Out Page")
window.geometry('718x400')
lbl = Label(window, text = "Are you checking your tool in or out?")
lbl.grid(column = 6, row =3)
rad1 = Radiobutton(window, text = 'Check In', value = 1)
rad2 = Radiobutton(window, text = 'Check Out', value = 2)
rad1.grid(column=6, row=4)
rad2.grid(column=6, row=5)
window.mainloop()


