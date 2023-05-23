# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34
def opposite(num):
    if num > 0 and type(num) == type(22.33):
        return float('-' + str(num))
    elif num > 0 and type(num) == type(2):
        return int('-' + str(num))
    elif num < 0 and type(num) == type(2.2):
        return float(str(num).replace('-', ''))
    elif num < 0 and type(num) == type(2):
        return int(str(num).replace('-', ''))
    else:
        return 0
