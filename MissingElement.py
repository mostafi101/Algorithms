# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:21:37 2016

@author: mostafijurrahaman
"""

def finder(arr1, arr2):
    count = {}
    output = list()
    
    for num in arr2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num in arr1:
        if num not in count or count[num] == 0:
            output.append(num)
        else:
            count[num] -= 1
    return output
    
finder([1,2,3,4,5,6],[6,4,3])