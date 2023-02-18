# A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.

# Write a function that can verify if the given integer n is a perfect number, and return True if it is, or return False if not.
# Examples

# n = 28 has the following divisors: 1, 2, 4, 7, 14, 28

# 1 + 2 + 4 + 7 + 14 = 28 therefore 28 is a perfect number, so you should return True

# Another example:

# n = 25 has the following divisors: 1, 5, 25

# 1 + 5 = 6 therefore 25 is not a perfect number, so you should return False

# Should return whether or not n is a perfect number
def is_perfect(n):
    if n <= 1:
        return False
  # Find the divisors of n and sum them up
    divisor_sum = 1  # Start with 1 because every number is divisible by 1
    i = 2  # Start with 2 because 1 is already accounted for
    while i * i <= n:
        if n % i == 0:
          # If i is a divisor, add both i and n/i to the divisor sum
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
        i += 1

  # Return True if the sum of the divisors is equal to n, False otherwise
    return divisor_sum == n
