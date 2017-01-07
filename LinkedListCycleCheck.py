# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:27:15 2017

@author: mostafijurrahaman
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.next != None:
        marker1 = marker1.next
        marker2 = marker2.next.next
        if marker2 == marker1:
            return True
    return False

from nose.tools import assert_equal
#CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

#CREATE NONCYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z

class TestCycleCheck(object):
    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        print "ALL TEST CASE PASSED"

t = TestCycleCheck()
t.test(cycle_check)