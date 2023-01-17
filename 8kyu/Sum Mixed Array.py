# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.
def sum_mix(arr):
    total = 0
    for a in arr:
        if a != type(0):
            total += int(a)
        else:
            total += a
    return total
