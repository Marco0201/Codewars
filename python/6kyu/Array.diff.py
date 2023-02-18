# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    if len(b) == 0:  # if b has no length, then it is empty or null. Just return a as the answer
        return a

    for i in b:
        for j in range(a.count(i)):
            a.remove(i)

    return a


# this solution also works for some reason.
#     for i in b:
#         if i in b:
#             for j in range(a.count(i)):
#                 a.remove(i)

#     return a
