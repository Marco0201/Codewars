# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

# If begin value is greater than the end, function should returns 0

# Examples

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)

# This is the first kata in the series:

#     Sum of a sequence (this kata)
#     Sum of a Sequence [Hard-Core Version]

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    elif begin_number == end_number:
        return begin_number
    elif begin_number < end_number:
        a = []
        for i in range(begin_number, end_number + 1, step):
            a.append(i)
            x = sum(a)
        return x
