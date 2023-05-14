# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.
def find_average(num):
    if num:
        return sum(num) / len(num)
    else:
        return 0
