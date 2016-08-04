def anagram(s1, s2):

    #Remove spaces and make lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    #Creating counting dictionary
    count = {}

    #Fill dictionary for first string
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Subtracting counts for second string
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True


print anagram('dog','god')
print anagram('clint eastwood','old west action')
print anagram('dd','aa')
