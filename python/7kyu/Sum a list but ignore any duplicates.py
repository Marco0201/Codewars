# Please write a function that sums a list, but ignores any duplicate items in the list.

# For instance, for the list [3, 4, 3, 6] , the function should return 10.

def sum_no_duplicates(l):
    num = 0
    for i in l:
        if l.count(i) == 1:
            num += i
    return num
# this solution also works
#     num = 0
#     test = {}
#     for i in l:
#         test[i] = test.get(i, 0) + 1

#     for j in l:
#         if test[j] == 1:
#             num += j
#     return num
