class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)

        for x in c.keys():
            if c[x] % 2 != 0:
                return False
        return True
