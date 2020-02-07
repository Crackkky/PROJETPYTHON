'''
Created on 3 Feb 2020

@author: crack
'''
from abc import ABC, abstractmethod
from tkinter import StringVar

class stuff(ABC):
    @abstractmethod
    def run(self, obj):
        pass
    
class stuffStringVar(stuff):
    def __init__(self):
        self.strVar = StringVar()
    
    def run(self, obj):
        self.strVar.set(obj)
