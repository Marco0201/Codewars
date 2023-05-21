# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34
def opposite(number):
    if number > 0 and type(number) == type(22.33):
        return float('-' + str(number))
    elif number > 0 and type(number) == type(2):
        return int('-' + str(number))
    elif number < 0 and type(number) == type(2.2):
        return float(str(number).replace('-', ''))
    elif number < 0 and type(number) == type(2):
        return int(str(number).replace('-', ''))
    else:
        return 0
