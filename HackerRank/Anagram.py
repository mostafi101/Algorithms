import sys

T= int(sys.stdin.readline())

for _ in xrange(T):
    s = sys.stdin.readline().replace(' ','').replace('\n','').lower()
    

    if len(s) % 2:
        print -1
    else:
        totalChange = 0
        count = {}

        for letter in s[: len(s)/2]:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
                
        

        for letter in s[len(s)/2:]:
            if letter in count and count[letter] > 0:
                count[letter] -= 1

        for k in count:
            totalChange += count[k]

        

        print totalChange

        
