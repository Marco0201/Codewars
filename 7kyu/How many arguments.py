# Create a function args_count, that returns the count of passed arguments

# args_count(1, 2, 3) -> 3
# args_count(1, 2, 3, 10) -> 4

def args_count(*numbers, **other):
    # single asterisk (*) is used to take in multiple arguements when you don't know how many there will be
    # double asterisk (**) is used to take in multiple arguements when you don't know how many there will be but will be in a dictionary
    return len(numbers) + len(other)
