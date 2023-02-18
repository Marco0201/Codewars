# vowelOne

# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

# All non-vowels including non alpha characters (spaces,commas etc.) should be included.

# Examples:

# vowelOne "abceios" -- "1001110"

# vowelOne "aeiou, abc" -- "1111100100"

def vowel_one(s):
    a = 'aeiouAEIOU'
    x = list(s)
    num = []
    l = 0
    while l <= len(x) - 1:
        if x[l] in a:
            num.append('1')
            l += 1
        else:
            num.append('0')
            l += 1
    return ''.join(num)
