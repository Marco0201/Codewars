# Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of values, second is multiplier. The function should filter all non-numeric values and multiply the rest by given multiplier.

def multiply_and_filter(seq, multiplier):
    nums = []
    l = 0
    while l <= len(seq) - 1:
        if type(seq[l]) == type(0) or type(seq[l]) == type(1.3):
            nums.append(seq[l] * multiplier)
            l += 1
        else:
            l += 1
    return nums
