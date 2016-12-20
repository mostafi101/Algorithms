# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 00:18:45 2016

@author: mostafijurrahaman
"""

def pair_sum(arr, k):
    #checking edge case
    if len(arr) < 2:
        return
    
    #Set for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        
        if target not in seen:
            seen.add(num)    
        else:
            output.add((min(target, num), max(target, num)))
            
    print '\n'.join(map(str,list(output)))
    print '*************'            
    return len(output)
    

#pair_sum([1,3,2,2],4)

from nose.tools import assert_equal
class PairTest(object):
    def test(self, sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print 'ALL TEST CASES PASSED'
        
t = PairTest()
t.test(pair_sum)