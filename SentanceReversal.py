# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:27:47 2016

@author: mostafijurrahaman
"""

def rev_word1(s):
    return " ".join(reversed(s.split()))

rev_word1('Hi Mostafij, are you ready to go')

def rev_word2(s):
    return " ".join(s.split()[::-1])

rev_word2('Hi Mostafij, are you ready to go')

#Solution
def rev_word(s):
    words = []
    length = len(s)
    space = [' ']
    i = 0
    
    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))
    
rev_word('Hi Mostafij, are you ready to go')