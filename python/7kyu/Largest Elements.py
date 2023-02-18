# Write a program that outputs the top n elements from a list.

# Example:

# largest(2, [7,6,5,4,3,2,1])
# # => [6,7]

def largest(n, xs):
    xs.sort()
    a = xs[::-1]
    l = 0
    num = []
    while l <= n - 1:
        num.append(a[l])
        l += 1

    num.sort()
    return num
