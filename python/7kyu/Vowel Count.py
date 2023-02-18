# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = 'aeiou'
    l = 0
    count = 0
    new = list(sentence)
    while l <= len(new) - 1:
        if new[l] in vowels:
            l += 1
            count += 1
        else:
            l += 1
    return count
