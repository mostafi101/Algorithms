# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:51:43 2017

@author: mostafijurrahaman
"""

class Queue2Stack(object):
    
    def __init__(self):
        #Two stack
        self.instack = []
        self.outstack = []
    
    def enqueue(self, item):
        self.instack.append(item)
    
    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        
queue = Queue2Stack()
for i in xrange(5):
    queue.enqueue(i)

for i in xrange(5):
    print queue.dequeue()