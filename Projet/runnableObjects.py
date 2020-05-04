'''
Created on 3 Feb 2020

@author: crack
'''
from abc import ABC, abstractmethod
from tkinter import StringVar


class RunnableObject(ABC):
    @abstractmethod
    def run(self, obj):
        pass


class RunnableStringVar(RunnableObject):
    def __init__(self):
        self.strVar = StringVar()

    def run(self, obj):
        self.strVar.set(obj)
