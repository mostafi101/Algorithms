# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:25:04 2017

@author: mostafijurrahaman
"""

def balance_check(s):
    
    if len(s)%2 !=0:
        return False
    
    opening = set('([{')
    matches = set([ ('(',')'), ('[',']'), ('{','}')])
    
    stack = []    
    
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0

print balance_check('[]')
print balance_check('[](')
print balance_check('[]()')
print balance_check('[{([{[]}]())}]')