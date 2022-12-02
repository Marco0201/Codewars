# You are given an array with several "even" words, one "odd" word, and some numbers mixed in.

# Determine if any of the numbers in the array is the index of the "odd" word. If so, return true, otherwise false.

def odd_ball(array):
    l = 0
    while l <= len(array) - 1:
        if array[l] != 'odd':
            l += 1
        else:
            break
    return l in array
