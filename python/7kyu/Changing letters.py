# When provided with a String, capitalize all vowels

# For example:

# Input : "Hello World!"

# Output : "HEllO WOrld!"

# Note: Y is not a vowel in this kata.

def swap(st):
    a = list(st)
    s = 'aeiou'
    l = 0
    while l <= len(a) - 1:
        if a[l] in s:
            a[l] = a[l].upper()
            l += 1
        else:
            l += 1
    return ''.join(a)
