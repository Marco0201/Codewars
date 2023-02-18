# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.
# Example

# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    pos_num = []
    neg_num = []
    if not arr:
        return []
    else:
        for i in arr:
            if i > 0:
                pos_num.append(i)
            elif i < 0:
                neg_num.append(i)

        return [len(pos_num), sum(neg_num)]
