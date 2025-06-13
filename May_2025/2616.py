class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()


        def can_make_pairs(max_diff):

            count = 0
            i = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= max_diff:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= p:
                    return True
            return count >= p

        left = 0 
        right = nums[-1] - nums[0]

        while left < right:

            mid = (left + right) // 2
            if can_make_pairs(mid):
                right = mid
            else: 
                left = mid + 1
        return left

