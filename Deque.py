# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:47:50 2017

@author: mostafijurrahaman
"""

class Deque(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
        
    def removeRear(self):
        return self.items.pop(0)
        
d = Deque()
print d.isEmpty()
print d.size()
d.addFront(5)
d.addFront(10)
d.addFront(15)
print d.removeRear()
d.addRear(5)
print d.removeRear()
d.addRear(5)
print d.removeFront()
print d.size()