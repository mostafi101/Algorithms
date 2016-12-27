# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:42:34 2016

@author: mostafijurrahaman
"""

def compress(s):
    result = ""
    if(len(s) == 0):
        return ""
    if(len(s) == 1):
        return s+"1"
        
    i = 1
    cnt = 1
    
    while i < len(s):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            result = result + s[i-1]+ str(cnt)
            cnt = 1
        i += 1
    result = result + s[i-1]+ str(cnt)
    return result

compress("AB")
compress("AAB")    
compress("ABBBBBCCCCC")

def compress_accurate(s):
    result = ""
    if(len(s) == 0):
        return ""
    if(len(s) == 1):
        return s
    
    i = 1
    cnt = 1
    
    while i < len(s):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if cnt > 1:
                result = result + s[i-1]+ str(cnt) 
            else:
                result = result + s[i-1]

            cnt = 1
        i += 1
    if cnt > 1:
        result = result + s[i-1]+ str(cnt) 
    else:
        result = result + s[i-1]
    return result

compress_accurate("AB")
compress_accurate("AAB")
compress_accurate("ABBBBBCCCCC")
