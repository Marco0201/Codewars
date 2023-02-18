# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return null in JS or Java, and None in Python.

# You can assume, that the input string has always non-zero length.
# Example

# first_non_repeated("test") # returns "e"
# first_non_repeated("teeter") # returns "r"
# first_non_repeated("trend") # returns "t" (all the characters are unique)
# first_non_repeated("aabbcc") # returns None (all the characters are repeated)

def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i

    # this method also works
#     words = {}
#     for i in s:
#         words[i] = words.get(i, 0) + 1
#     for j in s:
#         if words[j] == 1:
#             return j
