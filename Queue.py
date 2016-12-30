# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:29:22 2016

@author: mostafijurrahaman
"""

class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)

q = Queue()
print q.isEmpty()
q.enqueue(40)
q.enqueue(30)
print q.size()
print q.dequeue()
print q.size()
print q.isEmpty()
