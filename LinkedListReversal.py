# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:59:58 2017

@author: mostafijurrahaman
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
def reversal(head):
    current = head
    nextNode = None
    previous = None
    
    while current:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print a.value
print a.next.value
print b.next.value
print c.next.value

reversal(a)

print d.value
print d.next.value
print c.next.value
print b.next.value