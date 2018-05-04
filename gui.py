from appJar import gui

def styleButton(btn):
    app.setButtonBg(btn, "#337ab7")
    app.setButtonFg(btn, "white")
    app.setButtonCursor(btn,"hand2")
    app.setButtonRelief(btn,"groove")

def readFile():
    print("read File")

def solve():
    print("solve")


# setup GUI
app = gui("Root Finder")
app.setIcon("logo.gif")
app.setBg("#e2edff",override=True)
app.setFont(family="inherit")
#app.setSticky("new")
#app.setStretch("both")
app.setSticky("nesw")
app.setStretch("")

# Input Function Frame
app.startLabelFrame("Input Function",0,0)
app.setPadding([10,5])
app.addLabelEntry("f(x)=")
app.addLabel("orLabel","Or")
app.addFileEntry("fileEntry")

app.addButton("Load",readFile())
styleButton("Load")
app.stopLabelFrame()

# Method Frame
app.startLabelFrame("Method",0,1)
app.setPadding([10,5])
app.addLabelOptionBox("Method", ["- Bracketing Methods -", "Bisection", "False Position",
                        "- Open Methods -", "Fixed Point", "Newton-Raphson",
                        "Secant", "- Polynomials -", "Bierge Vieta"])
app.addLabelNumericEntry("Max Iterations")
app.setEntryDefault("Max Iterations", 50)
app.addLabelNumericEntry("Epsilon")
app.setEntryDefault("Epsilon", 0.0001)
app.addButton("Solve",solve)
styleButton("Solve")
app.stopLabelFrame()

# Output Frame
app.startTabbedFrame("TabbedFrame",1,0,colspan=2)
# Fast Mode Tab
app.startTab("Fast Mode")
app.addLabel("fastModeLabel", "Fast Mode Label")
app.setLabelWidth("fastModeLabel","110")
app.setLabelHeight("fastModeLabel","23")
app.stopTab()

# Single Step Mode
app.startTab("Single Step Mode")
app.addLabel("singleStepModeLabel", "Single Step Mode Label")
app.setLabelWidth("singleStepModeLabel","110")
app.setLabelHeight("singleStepModeLabel","23")
app.stopTab()

app.stopTabbedFrame()
app.go()