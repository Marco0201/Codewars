# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.

# The size will always be positive and will only use whole numbers.

def stringy(size):
    zero = '1'
    num = 0
    if size == 0:
        return ''
    elif size == 1:
        return zero
    else:
        while num <= size - 2:
            if zero[num] == '1':
                zero += '0'
                num += 1
            else:
                zero += '1'
                num += 1
    return zero
