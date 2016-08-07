import collections

def finder(arr1, arr2):
    
    #using default dict to avoid key error
    d = collections.defaultdict(int)

    #Adding counts for every instance of array1
    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# second approch

def finder2(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num

    return result

#test 
arr1 = [5,5,7,7]
arr2 = [5,7,7]

print finder(arr1,arr2)
print finder2(arr1,arr2)

