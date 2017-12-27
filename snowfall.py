
import random
import time
from tkinter import *
from cggsys.syslogic import *

class Snowfall(CGGPY):

    def __init__(self,cvs):
        super().__init__(cvs)
        self.m=[]
        for i in range(0,21):
            for j in range(0,41):
                self.m[len(self.m):] = [0]
        for i in range(0,19):
            r = random.randint(1,10)
            if r == 1:
                self.m[1*40 +i] = 1
            else:
                self.m[i*40+ 1] = 0

    def next(self):
        self.draw()

    def draw(self):
        self.cls()
        self.setcolor(6)
        for i in range(0,19):
            for j in range(0,39):
                r=random.randint(0,1)
                self.setcolor(7)
                if self.m[i*40+j]>0:
                    self.puth("star",j,i)

    def schroll(self):

        for i in range(0,39):
            r = random.randint(1,40)
            self.m[1*40+i] = 0
            if r == 1:
                self.m[1*40+i] = 2
            if r == 2:
                self.m[1*40+i] = 6 

        for i in range(18,0,-1):
            for j in range(0,39):
                self.m[(i+1)*40+j] = self.m[i*40+j] 
        self.draw() 


    def routine(self):
        self.schroll()

tk=Tk()
cvs=Canvas(tk,width=640,height=400)
cvs.pack()
sf=Snowfall(cvs)
while True:
    sf.routine()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)


