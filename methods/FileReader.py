class MyClass(object):
    file = 0
    method = 0
    eqn = 0
    tolerance = 0
    interval = "????"#TO DO HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    maxIteration = 0
    def __init__(self, path = ""):
        self.file = open(path, "r")
        
    def getResult(self):
        lines = self.file.readlines()

        self.method = int(lines[0])
        self.eqn = lines[1]
        self.interval = lines[2]
        self.tolerance = lines[3]
        self.maxIteration = lines[4]

        
        return self.method,self.eqn,self.interval,self.tolerance,self.maxIteration
