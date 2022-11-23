# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples

#     "foefet" is an anagram of "toffee"

#     "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    l = 0
    words = list(original)
    if len(original) == 1:
        return False
    else:
        for i in test:
            if i.lower() in original.lower():
                l += 1
            elif i.lower() not in original.lower():
                pass
        return l == len(words)
