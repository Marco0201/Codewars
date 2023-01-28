# Unfinished Loop - Bug Fixing #1

# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
def create_array(n):
    res = []
    for i in range(1, n+1):
        res.append(i)
    return res
