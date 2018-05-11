class MyClass(object):
    file = 0
    method = 0
    eqn = 0
    tolerance = 0
    interval = []#TO DO HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    maxIteration = 0
    validMethod = True
    def __init__(self, path = ""):
        self.file = open(path, "r")
        
    def getResult(self):
        lines = self.file.readlines()

        self.method = int(lines[0])
        
        self.eqn = lines[1]
        
        if self.method in (1,2,5):
            self.validMethod = True
            inter = lines[2]
            inter = inter.replace("[","")
            inter = inter.replace("]","")
            inter = inter.split(" ")
            for i in inter:
                self.interval.append(float(i))
        elif self.method in (3,4,6):
            self.validMethod = True
            inter = lines[2]
            inter = inter.replace("[","")
            inter = inter.replace("]","")
            self.interval.append(float(inter))
        elif self.method == 7:
            self.validMethod = True
        else:
            self.validMethod = False
            
        self.interval = lines[2]
        self.tolerance = float(lines[3])
        self.maxIteration = int(lines[4])

        
        return self.method,self.eqn,self.interval,self.tolerance,self.maxIteration,self.validMethod
