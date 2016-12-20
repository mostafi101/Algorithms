# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 22:03:03 2016

@author: mostafijurrahaman
"""

def anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    return sorted(s1) == sorted(s2)

#anagram('God', 'dog')
#anagram('clint eastwood ', 'old west action')

def anagram_optimal(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    #Eadge case check
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False
    
    for k in count:
        if count[k] != 0:
            return False
    
    return True
    
anagram_optimal('God', 'dog')
anagram_optimal('clint eastwood ', 'old west action')

from nose.tools import assert_equal
class AnagramTest(object):
    def test(self, sol):
        assert_equal(sol('go go go','gggooo'), True)
        assert_equal(sol('abc','bca'), True)
        assert_equal(sol('hi man', 'Hi       man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print 'ALL TEST CASE PASSED'
        
t = AnagramTest()
t.test(anagram_optimal)