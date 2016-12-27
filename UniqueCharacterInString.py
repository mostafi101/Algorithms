# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:29:28 2016

@author: mostafijurrahaman
"""

def uni_char1(s):
    s = s.lower()
    return len(set(s)) == len(s)

uni_char1("Ab")

def uni_char(s):
    s = s.lower()
    chars = set()
    
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True
    
uni_char("Ab")
uni_char("AABB")
uni_char("AaB")