
# Code
# Testcase
# Testcase
# Test Result
# 3043. Find the Length of the Longest Common Prefix
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two arrays with positive integers arr1 and arr2.

# A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.

# You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

# Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.



from narwhals import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_length = 0

        for num1 in arr1:
            for num2 in arr2:
                str_num1 = str(num1)
                str_num2 = str(num2)
                common_length = 0

                for digit1, digit2 in zip(str_num1, str_num2):
                    if digit1 == digit2:
                        common_length += 1
                    else:
                        break

                max_length = max(max_length, common_length)

        return max_length