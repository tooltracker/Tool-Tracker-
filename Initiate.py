
class tool(object):
    num = 0
    name = ""
    def create(self, num, name):
        self.num = num
        self.name = name
        checked = true
        return
    def getID(self):
        print(self.num)
        return
    def getTool(self):
        print(self.name)
    def status(self):
        print(self.checked)
        return
           
class student(object):
    studID = 0
    name = ""
    def create(self,studID,name,toolList):
        self.studID = studID
        self.name = name
        self.toolList = tools[]
        return
    def getStudID(self):
        print(self.studID)
        return
    def getName(self):
        print(self.name)
        return

def newStudent(idStud, name,toolList):
    student = Student()
    student.idStud = idStud
    student.name = name
    student.toolList = tools[]
    return student

def newTool(num, name):
    tool = tool()
    tool.num = num
    tool.name = name
    checked=true
    return tool
    

class admin():
    def addStudent(self, studID, name):
        self.newStudent(studID, name)
    
    def addTool(self, toolID, name):
        self.newTool(toolID, name)
        
