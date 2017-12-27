from tkinter import *

class CGGPY:

    def __init__(self,cvs):
        self.datainit()
        self.canvas=cvs
        self.canvas.create_rectangle(0,0,1300,800,fill="black")
        self.color='white'
        self.canvas.bind_all('<KeyPress-Left>',self.keyleft)
        self.canvas.bind_all('<KeyPress-Right>',self.keyright)
    
    def putc(self,str,chrctx,cx,cy):
        chr=self.chrname(str)
        for i in range(0,chrctx[2]):
            for j in range(0,chrctx[1]):
                if chr[i*chrctx[1]+j]==1:
                    if chrctx[0]==0: 
                        self.canvas.create_rectangle((cx+j)*4,(cy+i)*4,(cx+j)*4+4,(cy+i)*4+4,fill=self.color,outline=self.color,tag="obj")
                    if chrctx[0]==1: 
                        self.canvas.create_rectangle((cx+j)*2,cy*4+i*3,(cx+j)*2+1,cy*4+i*3+2,fill=self.color,outline=self.color,tag="obj")
                    if chrctx[0]==2: 
                        self.canvas.create_rectangle((cx+j)*2,(cy+i)*4,(cx+j)*2+1,(cy+i)*4+3,fill=self.color,outline=self.color,tag="obj")
    def cls(self):
        self.canvas.delete("obj")
    def print(self,str):
        self.canvas.create_text(70,440,text=str,fill=self.color)
    def printc(self,str,x,y):
        for i in range(0,len(str)):
            c=str[i]
            self.puth(c,x+i,y)
    def keyleft(self,ev):
        self.keyin="left"
    def keyright(self,ev):
        self.keyin="right"
    def chrname(self,str):
       if str=="a":
            return self.chra          
       if str=="b":
            return self.chrb          
       if str=="c":
            return self.chrc          
       if str=="d":
            return self.chrd          
       if str=="e":
            return self.chre          
       if str=="f":
            return self.chrf          
       if str=="g":
            return self.chrg          
       if str=="h":
            return self.chrh          
       if str=="i":
            return self.chri          
       if str=="j":
            return self.chrj          
       if str=="k":
            return self.chrk          
       if str=="l":
            return self.chrl          
       if str=="m":
            return self.chrm          
       if str=="n":
            return self.chrn          
       if str=="o":
            return self.chro          
       if str=="p":
            return self.chrp          
       if str=="q":
            return self.chrq          
       if str=="a":
            return self.chra          
       if str=="r":
            return self.chrr          
       if str=="s":
            return self.chrs          
       if str=="t":
            return self.chrt          
       if str=="u":
            return self.chru          
       if str=="v":
            return self.chrv          
       if str=="w":
            return self.chrw          
       if str=="x":
            return self.chrx          
       if str=="y":
            return self.chry          
       if str=="z":
            return self.chrz          
       if str=="0":
            return self.chrnum0          
       if str=="1":
            return self.chrnum1          
       if str=="2":
            return self.chrnum2          
       if str=="3":
            return self.chrnum3          
       if str=="4":
            return self.chrnum4          
       if str=="5":
            return self.chrnum5          
       if str=="6":
            return self.chrnum6          
       if str=="7":
            return self.chrnum7          
       if str=="8":
            return self.chrnum8          
       if str=="9":
            return self.chrnum9
       if str==" ":
            return self.chr0
       if str=="circle":
            return self.chr1
       if str=="heart":
            return self.chr2
       if str=="fill":
            return self.chr3
       if str=="sw":
            return self.chr4
       if str=="se":
            return self.chr5
       if str=="wave":
            return self.chr6
       if str=="spade":
            return self.chr7
       if str=="sharp":
            return self.chr8
       if str=="star":
            return self.chr9
       if str=="flag":
            return self.chr10
       if str=="slash":
            return self.chr11
       if str=="backslash":
            return self.chr12
       if str=="nw":
            return self.chr13
       if str=="ne":
            return self.chr14
       if str=="block":
            return self.chr15
       if str=="brick":
            return self.chr16
       if str=="equal":
            return self.chr17
       if str=="point":
            return self.chr18
       if str=="cornernw":
            return self.chr19
       if str=="cornerne":
            return self.chr20
       if str=="cornersw":
            return self.chr21
       if str=="cornerse":
            return self.chr22
       if str=="upbar":
            return self.chr23
       if str=="downbar":
            return self.chr24
       if str=="rightbar":
            return self.chr25
       if str=="leftbar":
            return self.chr26
       if str=="clover":
            return self.chr27
       if str=="larget":
            return self.chr28
       if str=="downarrow":
            return self.chr29
       if str==":":
            return self.chr30
       if str=="diamond":
            return self.chr31
       return self.chr0
          

    def setcolor(self,cc):
        if cc==0:
            self.color='black'
        if cc==1:
            self.color='blue'
        if cc==2:
            self.color='red'
        if cc==3:
            self.color='magenta'
        if cc==4:
            self.color='green'
        if cc==5:
            self.color='cyan'
        if cc==6:
            self.color='yellow'
        if cc==7:
            self.color='white'
    def put(self,str,x,y):
        ctx=[0,8,5]
        self.putc(str,ctx,x*8,y*5)

    def puth(self,str,x,y):
        ctx=[1,8,5]
        self.putc(str,ctx,x*8,y*5)

    def putl(self,str,x,y):
        ctx=[2,8,5]
        self.putc(str,ctx,x*8,y*5)

    def datainit(self):

        self.keyin=""
        
        self.chra=[0,0,0,1,1,0,0,0,
                   0,0,1,0,0,1,0,0,
                   0,1,1,1,1,1,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0]

        self.chrb=[0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,0,0]

        self.chrc=[0,0,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,1,0,
                   0,0,1,1,1,1,0,0]

        self.chrd=[0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,0,0]

        self.chre=[0,0,1,1,1,1,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,1,1,1,0,0,0,
                   0,1,0,0,0,0,0,0,
                   0,0,1,1,1,1,0,0]
        self.chrf=[0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,1,1,1,0,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,0,0]
        self.chrg=[0,0,1,1,1,1,1,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,0,1,1,1,1,0,0]
        self.chrh=[0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0]
        self.chri=[0,0,0,1,1,1,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,1,1,1,0,0]
        self.chrj=[0,0,0,1,1,1,1,0,
                   0,0,0,0,0,1,0,0,
                   0,1,0,0,0,1,0,0,
                   0,1,0,0,0,1,0,0,
                   0,0,1,1,1,0,0,0]
        self.chrk=[0,1,0,0,0,1,0,0,
                   0,1,0,0,1,0,0,0,
                   0,1,1,1,0,0,0,0,
                   0,1,0,0,1,0,0,0,
                   0,1,0,0,0,1,0,0]
        self.chrl=[0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,1,1,1,1,1,0]
        self.chrm=[0,1,0,0,0,0,0,1,
                   0,1,1,0,0,0,1,1,
                   0,1,0,1,0,1,0,1,
                   0,1,0,0,1,0,0,1,
                   0,1,0,0,0,0,0,1]
        self.chrn=[0,1,1,0,0,0,0,1,
                   0,1,0,1,0,0,0,1,
                   0,1,0,0,1,0,0,1,
                   0,1,0,0,0,1,0,1,
                   0,1,0,0,0,0,1,1]
        self.chro=[0,0,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,0,1,1,1,1,0,0]
        self.chrp=[0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,0,0,
                   0,1,0,0,0,0,0,0]
        self.chrq=[0,0,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,1,0,1,0,
                   0,1,0,0,0,1,0,0,
                   0,0,1,1,1,0,1,0]
        self.chrr=[0,1,1,1,1,1,0,0,
                   0,1,0,0,0,0,1,0,
                   0,1,1,1,1,1,0,0,
                   0,1,0,0,0,1,0,0,
                   0,1,0,0,0,0,1,0]
        self.chrs=[0,0,1,1,1,1,0,0,
                   0,1,0,0,0,0,0,0,
                   0,0,1,1,1,1,0,0,
                   0,0,0,0,0,0,1,0,
                   0,0,1,1,1,1,0,0]
        self.chrt=[0,0,1,1,1,1,1,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0]
        self.chru=[0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,0,1,1,1,1,0,0]
        self.chrv=[0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,1,0,0,0,0,1,0,
                   0,0,1,0,0,1,0,0,
                   0,0,0,1,1,0,0,0]
        self.chrw=[0,1,0,0,0,0,0,1,
                   0,1,0,0,0,0,0,1,
                   0,1,0,0,1,0,0,1,
                   0,1,0,1,0,1,0,1,
                   0,0,1,0,0,0,1,0]
        self.chrx=[0,0,1,0,0,0,1,0,
                   0,0,0,1,0,1,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,1,0,1,0,0,
                   0,0,1,0,0,0,1,0]
        self.chry=[0,0,1,0,0,0,1,0,
                   0,0,0,1,0,1,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0,
                   0,0,0,0,1,0,0,0]
        self.chrz=[0,1,1,1,1,1,1,0,
                   0,0,0,0,0,1,0,0,
                   0,0,0,1,1,0,0,0,
                   0,0,1,0,0,0,0,0,
                   0,1,1,1,1,1,1,0]
        self.chrex=[0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,1,0,0,0]
        self.chrnum0=[0,0,1,1,1,1,0,0,
                     0,1,0,0,0,1,1,0,
                     0,1,0,0,1,0,1,0,
                     0,1,0,1,0,0,1,0,
                     0,0,1,1,1,1,0,0]
        self.chrnum1=[0,0,0,0,1,0,0,0,
                     0,0,0,1,1,0,0,0,
                     0,0,0,0,1,0,0,0,
                     0,0,0,0,1,0,0,0,
                     0,0,0,1,1,1,0,0]
        self.chrnum2=[0,0,0,1,1,1,0,0,
                     0,0,1,0,0,0,1,0,
                     0,0,0,0,1,1,0,0,
                     0,0,0,1,0,0,0,0,
                     0,0,1,1,1,1,1,0]
        self.chrnum3=[0,0,1,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,0,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,1,1,1,1,0,0]
        self.chrnum4=[0,0,0,0,1,0,0,0,
                     0,0,0,1,1,0,0,0,
                     0,0,1,0,1,0,0,0,
                     0,1,1,1,1,1,1,0,
                     0,0,0,0,1,0,0,0]
        self.chrnum5=[0,1,1,1,1,1,0,0,
                     0,1,0,0,0,0,0,0,
                     0,1,1,1,1,1,0,0,
                     0,0,0,0,0,0,1,0,
                     0,1,1,1,1,1,0,0]
        self.chrnum6=[0,0,1,1,1,1,0,0,
                     0,1,0,0,0,0,0,0,
                     0,1,1,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,1,1,1,1,0,0]
        self.chrnum7=[0,0,1,1,1,1,1,0,
                     0,0,0,0,0,0,1,0,
                     0,0,0,0,0,1,0,0,
                     0,0,0,0,1,0,0,0,
                     0,0,0,1,0,0,0,0]
        self.chrnum8=[0,0,1,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,1,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,1,1,1,1,0,0]
        self.chrnum9=[0,0,1,1,1,1,0,0,
                     0,1,0,0,0,0,1,0,
                     0,0,1,1,1,1,1,0,
                     0,0,0,0,0,0,1,0,
                     0,0,1,1,1,1,0,0]
        self.chr0=[0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0]
        self.chr1=[0,0,1,1,1,1,0,0,
                  0,1,0,0,0,0,1,0,
                  0,1,0,0,0,0,1,0,
                  0,1,0,0,0,0,1,0,
                  0,0,1,1,1,1,0,0]
        self.chr2=[0,0,1,0,0,1,0,0,
                  0,1,1,1,1,1,1,0,
                  0,1,1,1,1,1,1,0,
                  0,0,1,1,1,1,0,0,
                  0,0,0,1,1,0,0,0]
        self.chr3=[1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1]
        self.chr4=[1,0,0,0,0,0,0,0,
                  1,1,1,0,0,0,0,0,
                  1,1,1,1,1,0,0,0,
                  1,1,1,1,1,1,1,0,
                  1,1,1,1,1,1,1,1]
        self.chr5=[0,0,0,0,0,0,0,1,
                  0,0,0,0,0,1,1,1,
                  0,0,0,1,1,1,1,1,
                  0,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1]
        self.chr6=[0,0,0,0,0,0,0,0,
                  0,0,1,1,0,0,0,0,
                  1,1,0,0,1,1,0,0,
                  0,0,0,0,0,0,1,1,
                  0,0,0,0,0,0,0,0]
        self.chr7=[0,0,0,1,1,0,0,0,
                  0,0,1,1,1,1,0,0,
                  0,1,1,1,1,1,1,0,
                  0,0,0,1,1,0,0,0,
                  0,0,1,1,1,1,0,0]
        self.chr8=[0,0,1,0,0,1,0,0,
                  1,1,1,1,1,1,1,1,
                  0,0,1,0,0,1,0,0,
                  1,1,1,1,1,1,1,1,
                  0,0,1,0,0,1,0,0]
        self.chr9=[0,1,0,0,0,0,1,0,
                  0,0,1,0,0,1,0,0,
                  0,1,1,1,1,1,1,0,
                  0,0,1,0,0,1,0,0,
                  0,1,0,0,0,0,1,0]
        self.chr10=[0,0,0,1,1,0,0,0,
                   0,0,0,1,1,1,1,0,
                   0,0,0,1,1,0,0,0,
                   0,0,0,1,1,0,0,0,
                   0,0,1,1,1,1,0,0]
        self.chr11=[0,0,0,0,0,0,0,1,
                   0,0,0,0,0,1,1,0,
                   0,0,0,1,1,0,0,0,
                   0,1,1,0,0,0,0,0,
                   1,0,0,0,0,0,0,0]
        self.chr12=[1,0,0,0,0,0,0,0,
                   0,1,1,0,0,0,0,0,
                   0,0,0,1,1,0,0,0,
                   0,0,0,0,0,1,1,0,
                   0,0,0,0,0,0,0,1]
        self.chr13=[1,1,1,1,1,1,1,1,
                   1,1,1,1,1,1,1,0,
                   1,1,1,1,1,0,0,0,
                   1,1,1,0,0,0,0,0,
                   1,0,0,0,0,0,0,0]
        self.chr14=[1,1,1,1,1,1,1,1,
                   0,1,1,1,1,1,1,1,
                   0,0,0,1,1,1,1,1,
                   0,0,0,0,0,1,1,1,
                   0,0,0,0,0,0,0,1]
        self.chr15=[0,0,0,0,0,0,0,0,
                   0,1,1,1,1,1,1,0,
                   0,1,1,1,1,1,1,0,
                   0,1,1,1,1,1,1,0,
                   0,0,0,0,0,0,0,0]
        self.chr16=[1,1,0,1,1,1,1,1,
                   1,1,0,1,1,1,1,1,
                   0,0,0,0,0,0,0,0,
                   1,1,1,1,1,0,1,1,
                   1,1,1,1,1,0,1,1]
        self.chr17=[0,0,0,0,0,0,0,0,
                   0,1,1,1,1,1,1,0,
                   0,0,0,0,0,0,0,0,
                   0,1,1,1,1,1,1,0,
                   0,0,0,0,0,0,0,0]
        self.chr18=[0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,
                   0,0,0,1,1,0,0,0,
                   0,0,0,1,1,0,0,0,
                   0,0,0,0,0,0,0,0]
        self.chr19=[1,1,1,1,1,1,1,1,
                   1,0,0,0,0,0,0,0,
                   1,0,0,0,0,0,0,0,
                   1,0,0,0,0,0,0,0,
                   1,0,0,0,0,0,0,0]
        self.chr20=[1,1,1,1,1,1,1,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1]
        self.chr21=[1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,1,1,1,1,1,1,1]
        self.chr22=[0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    1,1,1,1,1,1,1,1]
        self.chr23=[1,1,1,1,1,1,1,1,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0]
        self.chr24=[0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    1,1,1,1,1,1,1,1]
        self.chr25=[0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1,
                    0,0,0,0,0,0,0,1]
        self.chr26=[1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0]
        self.chr27=[0,0,0,1,1,0,0,0,
                    1,1,0,1,1,0,1,1,
                    1,1,0,0,0,0,1,1,
                    0,0,0,1,1,0,0,0,
                    0,0,1,1,1,1,0,0]
        self.chr28=[1,1,1,1,1,1,1,1,
                    0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0]
        self.chr29=[0,0,0,0,1,0,0,0,
                    0,0,0,0,1,0,0,0,
                    0,0,1,0,1,0,1,0,
                    0,0,0,1,1,1,0,0,
                    0,0,0,0,1,0,0,0]
        self.chr30=[0,0,0,0,0,0,0,0,
                    0,0,0,1,1,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,1,1,0,0,0,
                    0,0,0,0,0,0,0,0]
        self.chr31=[0,0,0,0,1,0,0,0,
                    0,0,0,1,1,1,0,0,
                    0,0,1,1,1,1,1,0,
                    0,0,0,1,1,1,0,0,
                    0,0,0,0,1,0,0,0]


