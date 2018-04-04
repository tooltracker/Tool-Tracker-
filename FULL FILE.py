import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('718x400')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #HAVE TO INSERT EACH NEW PAGE INTO THIS LIST IN PARENTHESES
        for F in (OpeningPage, InOrOut, PleaseScan, RejectID, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("OpeningPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.show()

#OPENING PAGE
class OpeningPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        lbl1 = tk.Label(self, text = "Welcome to Tool Tracker!")
        lbl1.grid(column=300, row=0)

        lbl2 = tk.Label(self, text = "Please enter Student ID:")
        lbl2.grid(column=300, row=100)
        self.idlist = []

        def update(number):
            #specify the length of the ID 
            if len(self.idlist)<6:
                #add the new number pressed into the array 
                self.idlist.append(number)
                print(self.idlist)
                ID=""
                for n in range(len(self.idlist)):
                    ID+=str(self.idlist[n])
                print(ID)
                lblBlank = tk.Label(self, text = ""+ ID)
                lblBlank.grid(column=400, row=100)

                lblID = tk.Label(self, text = print(self.idlist))
                lblID.grid(column=300, row=200)

        def clicked():
            update(1)
        btn1 = Button(self, text = "1", command = clicked)
        btn1.grid(column=299, row=600)

        def clicked():
            update(2)
        btn2 = Button(self, text = "2", command = clicked)
        btn2.grid(column=300, row=600)

        def clicked():
            update(3)
        btn3 = Button(self, text = "3", command = clicked)
        btn3.grid(column=301, row=600)

        def clicked():
            update(4)
        btn4 = Button(self, text = "4", command = clicked)
        btn4.grid(column=299, row=700)

        def clicked():
            update(5)
        btn5 = Button(self, text = "5", command = clicked)
        btn5.grid(column=300, row=700)

        def clicked():
            update(6)
        btn6 = Button(self, text = "6", command = clicked)
        btn6.grid(column=301, row=700)

        def clicked():
            update(7)
        btn7 = Button(self, text = "7", command = clicked)
        btn7.grid(column=299, row=800)

        def clicked():
            update(8)
        btn8 = Button(self, text = "8", command = clicked)
        btn8.grid(column=300, row=800)

        def clicked():
            update(9)
        btn9 = Button(self, text = "9", command = clicked)
        btn9.grid(column=301, row=800)

        def clicked():
            update(0)
        btn0 = Button(self, text = "0", command = clicked)
        btn0.grid(column=300, row=900)

        def update_submit():
            controller.show_frame("PleaseScan")
            
        btnsub = Button(self, text = "Submit ID", command = update_submit)
        btnsub.grid(column=300, row=1000)

    def show(self):
        # do whatever
        self.idlist = []
        lblID = tk.Label(self, text = print(self.idlist))
        lblID.grid(column=300, row=200)
        self.tkraise()

#THIS IS AN OPTION FOR IF THE ID IS NOT VAILD
class RejectID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl1 = Label(self, text = "This ID is not being recognized as valid. Please press the button and try again.")
        lbl1.grid(column=300, row=0)

        btn2 = Button(self, text = "Return to previous page", command= lambda: self.controller.show_frame('OpeningPage'))
        btn2.grid(column = 300, row= 600)
       
    def show(self):
        self.tkraise()

#ASKS THE PERSON IF THEY ARE CHECKING THE TOOL IN OR OUT
class InOrOut(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text = "Are you checking your tool in or out?")
        lbl.grid(column = 6, row =3)
        rad1 = Radiobutton(self, text = 'Check In', value = 1, command= lambda: self.controller.show_frame('OpeningPage'))
        rad2 = Radiobutton(self, text = 'Check Out', value = 2)
        rad1.grid(column=6, row=4)
        rad2.grid(column=6, row=5)

    def show(self):
        self.tkraise()

#TELLS THE PERSON TO SCAN THE ITEM
class PleaseScan(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text = "Please scan your tool!")
        lbl.grid(column=300, row=60)

     def show(self):
          self.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: self.controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: self.controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

    def show(self):
        self.tkraise()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

