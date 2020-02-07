'''
Created on 1 Feb 2020

@author: crack
'''

from tkinter import *
import tkinter as tk
from itertools import product
import re


class Application(tk.Frame):
    
    def __init__(self, master=None):
        self.current_calcul = StringVar()
        self.isDone = False
        self.canvas = None
        self.nbButton = 0
        self.buttonList = []
        self.radioVar = StringVar()
        self.radioVar.set(-1)
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()
        
    def number(self, numb): 
        if self.isDone:
            self.current_calcul.set("")
            self.isDone = False
            
        if(self.current_calcul.get() == ""):
            if(re.match('[0-9]', numb) is not None):
                self.current_calcul.set(numb)
        else:
            lastChar = self.current_calcul.get()[-1]
            if(re.match('^[0-9]', lastChar) is None):
                if(re.match('[0-9]', numb) is not None):
                    self.current_calcul.set(self.current_calcul.get()+numb)
            else:
                self.current_calcul.set(self.current_calcul.get()+numb)

        
    def calculate(self):
        res = eval(self.current_calcul.get())
        self.current_calcul.set(res)
        self.isDone=True
        
    def erase(self): 
        self.current_calcul.set("")
        
    def eraseCurrent(self):
        currentCalculStr = str(self.current_calcul.get())
        i=len(currentCalculStr)-1; currentChar = currentCalculStr[i]
        while(re.match('[0-9]', currentChar) is not None and i>=0):
            currentCalculStr = currentCalculStr[:-1]
            i-=1
            if(i >= 0): currentChar = currentCalculStr[i]
        self.current_calcul.set(currentCalculStr)
        
    def addToMemory(self):
        currentNumb=""
        addButton = True
        currentCalculStr = str(self.current_calcul.get())
        i=len(currentCalculStr)-1
        currentChar = currentCalculStr[i]
        
        while(re.match('[0-9]', currentChar) is not None and i>=0):
            currentNumb += currentChar
            i-=1
            currentChar = currentCalculStr[i]
        
        currentNumb = currentNumb[::-1]
        for butt in self.buttonList:
            if butt[1] == currentNumb:
                addButton = False
        
        if not(any(char.isdigit() for char in currentNumb)):
            addButton = False
            
        if addButton:
            button1 = tk.Radiobutton(self.canvas, text=currentNumb, padx = 20, value=currentNumb, 
                                      variable=self.radioVar)
            self.canvas.create_window(-20, 20+self.nbButton*20, window=button1, anchor="w")
            self.nbButton+=1
            self.buttonList.append((button1, currentNumb))
            
    def getFromMemory(self):
        print(self.current_calcul.get()[:-1])
        if self.current_calcul.get() == "" or re.match('[0-9]', self.current_calcul.get()[-1:]) is not None:
            self.current_calcul.set(self.radioVar.get())
        else:
            self.number(self.radioVar.get())
            
    def destroyOneButton(self):
        buttonToDestroy = None;
              
        for butt in self.buttonList:
            if butt[1] == self.radioVar.get():
                buttonToDestroy = butt
            butt[0].destroy()
        self.buttonList.remove(buttonToDestroy)
        self.nbButton-=1
        
        tempList = []
        tempNbButton = 0
        for i in range(0, self.nbButton):
            button1 = tk.Radiobutton(self.canvas, text=self.buttonList[i][1], 
                                    padx = 20, value=self.buttonList[i][1], 
                                    variable=self.radioVar)
            self.canvas.create_window(-20, 20+tempNbButton*20, window=button1, anchor="w")
            tempNbButton+=1
            tempList.append((button1, self.buttonList[i][1]))
            
        self.buttonList = tempList
        self.nbButton = tempNbButton
        
    def destroyEverything(self):
        for butt in self.buttonList:
            butt[0].destroy()
            
        self.buttonList = []
        self.nbButton = 0
        
        self.current_calcul.set("")
    
    def createWidgets(self):
        calculation_label = tk.Label(self, textvariable = self.current_calcul,
                                    borderwidth=2, relief="sunken")
        calculation_label.grid(row=0, column=2, columnspan=8, rowspan=2, 
                               sticky="nsew")
        
        self.canvas = Canvas(self, width = 100, height = 180, 
                        scrollregion=(0,0,500,500), borderwidth=2, relief="sunken")
        self.canvas.grid(row=0, column=0, rowspan=5, sticky="nsew")
        hbar=Scrollbar(self, orient=HORIZONTAL)
        hbar.grid(row=5, column=0, columnspan=3, sticky="nsew")
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(self,orient=VERTICAL)
        vbar.grid(row=2, column=2, rowspan=3, sticky="nsew")
        vbar.config(command=self.canvas.yview)
        
        
        button = tk.Button(self, text="M+",  command=lambda: self.addToMemory())
        button.grid(row=2, column=3, columnspan=2, sticky="nsew")
        
        button = tk.Button(self, text="M-",  command=lambda: self.getFromMemory())
        button.grid(row=3, column=3, columnspan=2, sticky="nsew")
        
        button = tk.Button(self, text="Suppr",  command=lambda: self.destroyOneButton())
        button.grid(row=4, column=3, columnspan=2, sticky="nsew")
        
        button = tk.Button(self, text="RAZ",  command=lambda: self.destroyEverything())
        button.grid(row=5, column=3, columnspan=2, sticky="nsew")
        
        
        counter = 1
        for row, col in product(range(4,1, -1), range(5,8)):
            button = tk.Button(self, text=""+str(counter),  
                               command=lambda x=str(counter): self.number(x))
            button.grid(row=row, column=col, sticky="nsew")
            counter += 1
            
        button = tk.Button(self, text="0",  command=lambda x="0": self.number(x))
        button.grid(row=5, column=5, sticky="nsew")
        
        button = tk.Button(self, text="=",  command=lambda : self.calculate())
        button.grid(row=5, column=6, columnspan=2, sticky="nsew")
        
        
        button = tk.Button(self, text="/",  command=lambda x="/": self.number(x))
        button.grid(row=2, column=8, sticky="nsew")
        
        button = tk.Button(self, text="*",  command=lambda x="*": self.number(x))
        button.grid(row=3, column=8, sticky="nsew")
        
        button = tk.Button(self, text="-",  command=lambda x="-": self.number(x))
        button.grid(row=4, column=8, sticky="nsew")
        
        button = tk.Button(self, text="+",  command=lambda x="+": self.number(x))
        button.grid(row=5, column=8, sticky="nsew")

        
        button = tk.Button(self, text="C",  command=lambda: self.erase())
        button.grid(row=2, column=9, rowspan=2, sticky="nsew")
        
        button = tk.Button(self, text="CE",  command=lambda: self.eraseCurrent())
        button.grid(row=4, column=9, rowspan=2, sticky="nsew")
        







root = tk.Tk()

app = Application(master = root)


app.mainloop()


