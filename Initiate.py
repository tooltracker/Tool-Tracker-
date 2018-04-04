
class tool(object):
    num = 0
    name = ""
    def create(self, num, name):
        self.num = num
        self.name = name
        return
    def getID(self):
        print(self.num)
        return
    def getTool(self):
        print(self.name)
        return
           
class student(object):
    studID = 0
    name = ""
    def create(self,studID,name):
        self.studID = studID
        self.name = name
        return
    def getStudID(self):
        print(self.studID)
        return
    def getName(self):
        print(self.name)
        return

def newStudent(idStud, name):
    student = Student()
    student.idStud = idStud
    student.name = name
    return student

def newTool(num, name):
    tool = tool()
    tool.num = num
    tool.name = name
    return tool
    

class admin():
    def addStudent(self, studID, name):
        self.newStudent(studID, name)
    
    def addTool(self, toolID, tool):
        self.newTool(toolID, tool)
        
