# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:14:57 2016

@author: mostafijurrahaman
"""

class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
        
stack = Stack()
stack.push(30)
print stack.pop()
print stack.pop()
print stack.isEmpty()