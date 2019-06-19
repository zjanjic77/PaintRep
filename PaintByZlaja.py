from Tkinter import *
import tkFileDialog
import tkMessageBox


# Base class for color and start (first) point
class GrafLik:
    color = 'black'
    point = (0, 0)  # All points have x and y components

    def __init__(self, boja, t1):
        self.point = t1
        self.color = boja

    def Draw(self):
        return

    def setColor(self, boja):
        self.color = boja
        return

    def getColor(self):
        return self.color


# Class for drawing line
class Line(GrafLik):
    drpoint = (0, 0)

    def __init__(self, boja, t1, t2):
        GrafLik.__init__(self, boja, t1)
        self.drpoint = t2

    def Draw(self, canvas):
        canvas.create_line((self.point, self.drpoint), fill=self.color)
        return


# Class for drawing Triangle
class Triangle(Line):
    trpoint = (0, 0)

    def __init__(self, boja, t1, t2, t3):
        Line.__init__(self, boja, t1, t2)
        self.trpoint = t3

    def Draw(self, canvas):
        canvas.create_polygon((self.point, self.drpoint, self.trpoint),
                              fill='', outline=self.color)
        return


# Class for drawing Polygon
class Polygon(GrafLik):
    polje = ()

    def __init__(self, boja, p):
        GrafLik.__init__(self, boja, (0, 0))
        self.polje = p

    def Draw(self, canvas):
        canvas.create_polygon(self.polje, fill='', outline=self.color)
        return


# Class for drawing Rectangle
class Rectangle(GrafLik):
    drpoint = (0, 0)

    def __init__(self, boja, t1, t2):
        GrafLik.__init__(self, boja, t1)
        self.drpoint = t2

    def Draw(self, canvas):
        canvas.create_rectangle(self.point, self.point[0] + self.drpoint[0],
                                self.point[1] + self.drpoint[1], fill='',
                                outline=self.color)
        return


# Class for drawing Circle
class Circle(GrafLik):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, boja, t1, r):
        GrafLik.__init__(self, boja, t1)
        self.x1 = self.point[0] - r
        self.y1 = self.point[1] - r
        self.x2 = self.point[0] + r
        self.y2 = self.point[1] + r

    def Draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill='',
                           outline=self.color)
        return


# Class for drawing Ellipse
class Ellipse(Circle):
    def __init__(self, boja, t1, r1, r2):
        Circle.__init__(self, boja, t1, r1)
        self.y1 = self.point[1] - r2
        self.y2 = self.point[1] + r2


# Class for application with GUI
class Application(Frame):
    # function for clear button
    def Clear(self):
        self.C.delete('all')
        self.commandLine.delete(0, END)

    # drawing shape from command line
    def drawComamnd(self, agrc):
        # get string from command line and clear it
        command = self.commandLine.get().lower()
        self.commandLine.delete(0, END)
        command = command.rstrip()
        lineContents = command.split(' ')
        # parse command and draw shape
        try:
            if lineContents[0] == 'line':
                lajna = Line(
                            lineContents[1],
                            (float(lineContents[2]), float(lineContents[3])),
                            (float(lineContents[4]), float(lineContents[5])))
                lajna.Draw(self.C)
                return

            if lineContents[0] == 'triangle':
                trokutic = Triangle(
                              lineContents[1],
                              (float(lineContents[2]), float(lineContents[3])),
                              (float(lineContents[4]), float(lineContents[5])),
                              (float(lineContents[6]), float(lineContents[7])))
                trokutic.Draw(self.C)
                return
            if lineContents[0] == 'rectangle':
                pravoukaonik = Rectangle(
                            lineContents[1],
                            (float(lineContents[2]), float(lineContents[3])),
                            (float(lineContents[4]), float(lineContents[5])))
                pravoukaonik.Draw(self.C)
                return
            if lineContents[0] == 'circle':
                kruzic = Circle(
                            lineContents[1],
                            (float(lineContents[2]), float(lineContents[3])),
                            float(lineContents[4]))
                kruzic.Draw(self.C)
                return
            if lineContents[0] == 'polygon':
                duljina = len(lineContents)
                mnogougaonik = Polygon(lineContents[1],
                                       lineContents[2:duljina])
                mnogougaonik.Draw(self.C)
                return
            if lineContents[0] == 'ellipse':
                cepelin = Ellipse(
                             lineContents[1],
                             (float(lineContents[2]), float(lineContents[3])),
                             float(lineContents[4]), float(lineContents[5]))
                cepelin.Draw(self.C)
                return
        except:
            pass

    # creating GUI objects
    def GUI(self):
        self.C = Canvas(self, bg="#999999", height=800, width=1000)
        self.C.pack(fill=BOTH, expand=YES)
        self.commandLabel = Label(self, text="Command:")
        self.commandLabel.pack(side=LEFT)
        self.commandLine = Entry(self, width=100)
        self.commandLine.pack(side=LEFT)
        self.commandLine.bind('<Return>', self.drawComamnd)
        self.clearButton = Button(self, text="Clear", command=self.Clear)
        self.clearButton.pack(side=RIGHT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.GUI()

root = Tk()
root.title('Paint by Zl@ja')
root.resizable(height=False, width=False)
app = Application(root)
app.mainloop()
