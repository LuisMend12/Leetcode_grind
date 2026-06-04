# 3751. Total Waviness of Numbers in Range I
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integers num1 and num2 representing an inclusive range [num1, num2].

# The waviness of a number is defined as the total count of its peaks and valleys:

# A digit is a peak if it is strictly greater than both of its immediate neighbors.
# A digit is a valley if it is strictly less than both of its immediate neighbors.
# The first and last digits of a number cannot be peaks or valleys.
# Any number with fewer than 3 digits has a waviness of 0.
# Return the total sum of waviness for all numbers in the range [num1, num2].


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                left, curr, right = int(s[i-1]), int(s[i]), int(s[i+1])
                if curr > left and curr > right:   # peak
                    total += 1
                elif curr < left and curr < right: # valley
                    total += 1
        return total
