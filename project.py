import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
from scanTool import scan
from scanTool import getUID
import fileinput
import datetime
#OVERALL PAGE FLOW:
    #FIRST PAGE: opening page where someone signs in with their student ID or can go to the info page
    #POTENTIAL SECOND: rejecting an ID if it is not valid, if not rejected then go to the scanning page
    #THIRD: checking in/out --> atuomatically switches to:
    #FOURTH: please scan your item
        #IF PRESS OUT -->THANK YOU
        #IF PRESS IN -->  how was your experience

#This is the place where all 'global' variables that go across pages are initialized in the controller
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('800x480')
        self.toolId = 0
        self.toolList = ["Hammer", "Screwdriver", "Chisel", "Nail", "Tape Measure", "Bandsaw", "Table Saw", "Drill Press", "Monkey Wrench", "Utility Knife"]
        self.statusList = [True, True, True, True, True, True, True, True, True, True]
        self.inorout = 1
        self.userLog = ['','','','','','','','','','']
        self.ID = ''
        self.idlist = []
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.avgRate = [10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0]
        self.count = [0,0,0,0,0,0,0,0,0,0]
        self.rating = [0,0,0,0,0,0,0,0,0,0]
        self.rate = 0
        self.lblBlank = tk.Label(self, text = "")

        #Updating Status of tools from text file
        g = open('Status.txt', 'r')
        list = [0,1,2,3,4,5,6,7,8,9]
        num = 0
        for line in g:
            if line == 'Checked In\n':
                self.statusList[num] = True
            else:
                self.statusList[num] = False
            num = num + 1       
        g.close()
       
        
        #Updating User base from text file
        num = 0
        print(len(self.userLog))
        print(self.userLog[0])
        h = open('User.txt', 'r')
        for line in h:
            if line != '\n':
               
                self.userLog[num] = line
            
            num = num + 1
        h.close()
        
        num = 0
        #Updating Average rage from text file
        i = open('rating.txt','r')
        for line in i:
            self.rating[num] = float(line)
            num = num + 1
        i.close()
        
        num = 0
        j = open('count.txt', 'r')
        for line in j:
            self.count[num] = float(line)
            num = num+1
        j.close()
        
        num = 0
        k = open('avgRate.txt', 'r')
        for line in k:
            self.avgRate[num] = float(line)
            num = num+1
        k.close()
        
        
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #Every page included in the system goes into this statement below
        for F in (OpeningPage, InOrOut, PleaseScan, Ghost, RejectID, ThankYou, Experience, InfoPage, PleaseScan, AlreadyIn, AlreadyOut):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        #begins with the opening page
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
        self.idlist = []
        
        self.controller.lblBlank = tk.Label(self, text = "")
        self.controller.lblBlank.grid(column=400, row=100)
        
        lbl1 = tk.Label(self, text = "Welcome to Tool Tracker!")
        lbl1.grid(column=300, row=0)

        lbl2 = tk.Label(self, text = "Please enter Student ID:")
        lbl2.grid(column=300, row=100)
        
        #Takes someone to the info page automatically.
        gotoinfo = Button(self, text = "Info Page", command = lambda: self.controller.show_frame('InfoPage'))
        gotoinfo.grid(column = 300, row = 1500)
        
        #These are our student ID's, which act as the only acceptable ones for our system. Anything else is rejected.
        self.accepted0 = [4,4,8,3,6,3]
        self.accepted1 = [4,5,5,5,9,7]
        self.accepted2 = [4,5,7,5,6,5]
        self.accepted3 = [1,2,3,4,5,6]
        
        #This prints out the ID as someone presses the numbered buttons. 
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
                self.controller.studentID = ID 

               # lblID = tk.Label(self, text = self.idlist)
               #lblID.grid(column=300, row=200)

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
            if self.idlist == self.accepted0 or self.idlist == self.accepted1 or self.idlist == self.accepted2 or self.idlist == self.accepted3:
                self.controller.show_frame('PleaseScan')
            else:
              self.controller.show_frame("RejectID")
            
        btnsub = Button(self, text = "Submit ID", command = update_submit)
        btnsub.grid(column=300, row=1000)

    def show(self):
        self.idlist = []
        lblID = tk.Label(self, text = self.idlist)
        lblID.grid(column=300, row=200)
        self.tkraise()

#THIS SHOWS IF THE ID IS NOT VAILD
class RejectID(tk.Frame):
        
    def combine():
        self.controller.show_frame('OpeningPage')
        res = "___________"
        self.controller.lblBlank.configure(text=res)
        lblBlank = tk.Label(self, text = "")
    
    def __init__(self, parent, controller):
                
        def combine():
            self.controller.show_frame('OpeningPage')
            res = "     "
            self.controller.lblBlank.configure(text=res)
            
            #lblBlank = tk.Label(self, text = "")
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl1 = Label(self, text = "This ID is not being recognized as valid. Please press the button and try again.")
        lbl1.grid(column=300, row=0)
        ID = " "

        #btn2 = Button(self, text = "Return to previous page", command = lambda:self.controller.show_frame('OpeningPage'))
        btn2 = Button(self, text = "Return to previous page", command = combine)
        btn2.grid(column = 300, row= 600)
  
    def show(self):
        self.tkraise()

#TELLS THE PERSON TO SCAN THE ITEM
class PleaseScan(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text = "SCANNING PAGE")
        lbl.grid(column=300, row=60)
        
        #press this button THEN scan the tool
        btnNext = Button(self, text = "Press Me & Then Scan to the Right of the Console", command= lambda: self.controller.show_frame('Ghost'))
        btnNext.grid(column = 300, row= 70)

     def show(self):
         self.tkraise()

#This page is never actually seen, but it helps in the transition when a chip is scanned.
class Ghost(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
         
    def show(self):
        self.tkraise()
        id = scan()
        print('Returned: ' + str(id))
        self.controller.toolId = id      
        self.controller.nameTool = self.controller.toolList[self.controller.toolId -1]

        print(str(self.controller.toolId))
        self.controller.show_frame('InOrOut')

#ASKS THE PERSON IF THEY ARE CHECKING THE TOOL IN OR OUT
class InOrOut(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text = "Are you checking your tool in or out?")
        lbl.grid(column = 6, row =3)
        #Takes you to different pages based on if you are checking in or out.
        
        def checkedIn():
            if self.controller.statusList[self.controller.toolId-1]:
                self.controller.show_frame('AlreadyIn')
            else:
                self.controller.show_frame('Experience')
            
        rad1 = Button(self, text = 'Check In', command = checkedIn)
        rad1.grid(column=6, row=4)
        
        def checkedOut():
            if self.controller.statusList[self.controller.toolId-1]:
                self.controller.show_frame('ThankYou')
            else:
                self.controller.show_frame('AlreadyOut')
        rad2 = Button(self, text = 'Check Out',command= checkedOut)
        rad2.grid(column=6, row=5)
        
        #scanTool.updatevalue()
        #toolList.append(0,self.controller.toolId)
        #print(toolList)
        
    def show(self):
        print('Id: ' + str(self.controller.toolId))
        #This goes through the array and prints out which tool they have based on how we put them into the name array.
        lblname = Label(self, text = "You have a " + self.controller.toolList[self.controller.toolId-1])
        lblname.grid(column = 6, row = 6)
        self.tkraise()
                        
#ASKS THE PERSON IF THEY ARE CHECKING A TOOL IN HOW THEIR EXPERIENCE WAS
class Experience(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        lbl1 = Label(self, text = "Please rate the condition of the tool on a scale from 1-10.")
        lbl1.grid(column=300, row=0)

        lblcom = Label(self, text = " ")
        lblcom.grid(column=300, row=70)

        #This system provides different messages to a user based on how they rate their experience.
        #poor experience
      #  def clicked():
       #     lblcom.configure(text = "We are sorry for your experience. Please consult the professor.")
        #    self.controller.rate = 1.0
        #rad1 = Radiobutton(self, text = '1', value = 1, command = clicked)
        #rad1.grid(column = 100, row = 30)
        def clicked():
            lblcom.configure(text = "We are sorry for your experience. Please consult the professor.")
            self.controller.rate = 1.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            #now = datetime.datetime.now()
            #line1 = str(now) + "\n"
            f.write(string)
            #f.write(line1)
            f.close()
        rad1 = Radiobutton(self, text = '1', value = 1, command = clicked)
        rad1.grid(column = 100, row = 30)
            
        def clicked():
            lblcom.configure(text = "We are sorry for your experience. Please consult the professor.")
            self.controller.rate = 2.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad2 = Radiobutton(self, text = '2', value = 2, command = clicked)
        rad2.grid(column = 100, row = 31)
        def clicked():
            lblcom.configure(text = "We are sorry for your experience. Please consult the professor.")
            self.controller.rate = 3.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad3 = Radiobutton(self, text = '3', value = 3, command = clicked)
        rad3.grid(column = 100, row = 32)

        #average experience
        def clicked():
            lblcom.configure(text = "Please consult the professor to elaborate about what could have been improved.")
            self.controller.rate = 4.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad4 = Radiobutton(self, text = '4', value = 4, command = clicked)
        rad4.grid(column = 100, row = 40)
        def clicked():
            lblcom.configure(text = "Please consult the professor to elaborate about what could have been improved.")
            self.controller.rate = 5.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad5 = Radiobutton(self, text = '5', value = 5, command = clicked)
        rad5.grid(column = 100, row  = 41)
        def clicked():
            lblcom.configure(text = "Please consult the professor to elaborate about what could have been improved.")
            self.controller.rate = 6.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad6 = Radiobutton(self, text = '6', value = 6, command = clicked)
        rad6.grid(column = 100, row = 42)

        #good experience
        def clicked():
            lblcom.configure(text = "Awesome, thank you!")
            self.controller.rate = 7.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad7 = Radiobutton(self, text = '7', value = 7, command = clicked)
        rad7.grid(column = 100, row = 43)
        def clicked():
            lblcom.configure(text = "Awesome, thank you!")
            self.controller.rate = 8.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad8= Radiobutton(self, text = '8', value = 8, command = clicked)
        rad8.grid(column = 100, row = 50)
        def clicked():
            lblcom.configure(text = "Awesome, thank you!")
            self.controller.rate = 9.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad9 = Radiobutton(self, text = '9', value = 9, command = clicked)
        rad9.grid(column = 100, row=51)
        def clicked():
            lblcom.configure(text = "Awesome, thank you!")
            self.controller.rate = 10.0
            f = open('Textfile2.txt', 'a')
            now = datetime.datetime.now()
            string = 'Checked Out By:' + self.controller.studentID + ' At:' + str(now)+ ' with a rating of: ' + str(self.controller.rate)
            f.write(string)
        rad10 = Radiobutton(self, text = '10', value = 10, command = clicked)
        rad10.grid(column = 100, row = 52)

        btn2 = Button(self, text = "Return to home page", command= lambda: self.controller.show_frame('OpeningPage'))
        btn2.grid(column = 300, row= 60)
            
     def show(self):
        
        f = open('Textfile2.txt', 'a')
     #   for index in range(len(self.controller.statusList)):
        #      printRate=  self.controller.rating[index] 
        string = 'Checked In By:' + self.controller.studentID + 'With a Rating of:' + str(self.controller.rate)                                                                            
        now = datetime.datetime.now()
        line1 = str(now) + "\n"
        f.write(string)
        f.write(line1)
        f.close()
        
        #avg
        self.controller.count[self.controller.toolId-1] = self.controller.count[self.controller.toolId-1]+1
        for index in range(len(self.controller.statusList)):
            #print(self.controller.rating)
            open('rating.txt', 'w').close()
            self.controller.rating[self.controller.toolId-1] =  self.controller.rating[self.controller.toolId-1] + self.controller.rate
            
            if self.controller.rate != 0.0:
                print('rate :' +str(self.controller.rating[index]))
            self.controller.avgRate[index] = self.controller.rating[index] / self.controller.count[index]
            open('avgRate.txt', 'w').close()
            i = open('avgRate.txt', 'a')
            for eliot in range(len(self.controller.avgRate)):
                z = str(self.controller.avgRate[eliot]) + '\n'
                i.write(z)
            i.close()
        
        
        open('count.txt', 'w').close()
        t = open('count.txt', 'a')
        for index in range(10):
            a = str(self.controller.count[index])+'\n'
            t.write(a)
        t.close()
        
        
 
        self.controller.inorout = 1
        self.controller.statusList[self.controller.toolId-1] = True
        #self.controller.count[self.controller.toolId-1] = self.controller.count[self.controller.toolId-1] + 1
        self.tkraise()
          
#LAST MESSAGE TO SOMEONE WHO IS CHECKING A TOOL OUT, THANK YOU
class ThankYou(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text = "Thank you!")
        lbl.grid(column=300, row=60)
        
        btn2 = Button(self, text = "Return to home page", command= lambda: self.controller.show_frame('OpeningPage'))
        btn2.grid(column = 300, row= 70)
        
     def show(self):
        #scan()
         
        f = open('Textfile2.txt', 'a')
        string = 'Checked Out By:' + self.controller.studentID + ' At:'
        now = datetime.datetime.now()
        line1 = str(now) + "\n"
        f.write(string)
        f.write(line1)
        f.close()
        
        self.controller.statusList[self.controller.toolId-1] = False
        self.controller.userLog[self.controller.toolId-1] = self.controller.studentID      
        self.controller.inorout = 0
        self.tkraise()

class InfoPage(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        lbl1 = Label(self, text = "Welcome to the Info Page!")
        lbl1.grid(column = 300, row =0)
        
        btn2 = Button(self, text = "Return to home page", command= lambda: self.controller.show_frame('OpeningPage'))
        btn2.grid(column = 300, row= 15)
        
    def show(self):
        #putting controller of the Ids
        lbl2 = Label(self, text = "Current Tools: ")
        lbl2.grid(column = 200, row =2)
      
        for index in range(len(self.controller.toolList)):
            lbl3 = Label(self,text = self.controller.toolList[index])
            lbl3.grid(column = 200, row =index + 3)
        
        lbl4 = Label(self,text = "Status: ")
        lbl4.grid(column = 275, row = 2)
        
        lbl5 = Label(self,text = "Rating: ")
        lbl5.grid(column = 400, row = 2)
        
        print('Rate: '+str(self.controller.rate))
        print(self.controller.count[self.controller.toolId-1])
        
            
        for index in range(len(self.controller.statusList)):
            #print(self.controller.rating)
            lbl6 = Label(self,text = self.controller.avgRate[index])
            lbl6.grid(column = 400, row =index+3)
        
        

     #Configuring file to match data stored in arrays 
        open('Status.txt', 'w').close()
        f = open('Status.txt', 'a')
        for index in range(10):
            if self.controller.statusList[index]:
                x = 'Checked In\n'
                f.write(x)
            else:
                y = 'Checked Out\n'
                f.write(y)
        f.close()
        for index in range(len(self.controller.statusList)):
            if self.controller.statusList[index]:
                status = Label(self, text = "Checked In")
            else:
                status = Label(self, text = "Checked Out")
            status.grid(column = 275, row = index +3)
            
        userLog = Label(self,text = "User: ")
        userLog.grid(column = 300, row = 2)
        open('User.txt', 'w').close()
        g = open('User.txt', 'a')
        for index in range(10):
            y = self.controller.userLog[index] 
            g.write(y)
        g.close()        
        for index in range(len(self.controller.userLog)):
            lbl5 = Label(self,text = self.controller.userLog[index])
            lbl5.grid(column = 300, row = index + 3)        
         
        self.tkraise()
        
class AlreadyIn(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        lbl1 = Label(self,text = "This tool is already checked in. Please scan the tool again.")
        lbl1.grid(column = 300, row = 1)
        
        btn1= Button(self, text = "Return to scan page", command= lambda: self.controller.show_frame('PleaseScan'))
        btn1.grid(column = 300, row= 2)
    
    def show(self):
        self.tkraise()

class AlreadyOut(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
     
        lbl1 = Label(self,text = "This tool is already checked out. Please scan the tool again.")
        lbl1.grid(column = 300, row = 1)
       
        btn1= Button(self, text = "Return to scan page", command= lambda: self.controller.show_frame('PleaseScan'))
        btn1.grid(column = 300, row= 2)
        
    def show(self):
        self.tkraise()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
