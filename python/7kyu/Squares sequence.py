# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative or zero, return an empty array/list.
# Examples

# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]

def squares(x, n):
    num = [x]
    l = 0
    if n <= l:
        return []
    else:
        for i in range(n - 1):
            num.append(num[l] ** 2)
            l += 1
        return num
