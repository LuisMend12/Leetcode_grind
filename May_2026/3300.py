# You are given an integer array nums.

# You replace each element in nums with the sum of its digits.

# Return the minimum element in nums after all replacements


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(d) for d in str(n)) for n in nums)
