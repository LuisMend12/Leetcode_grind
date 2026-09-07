# You are given an intenger array nums and an integer sum. In one operation, choose an elemnet with currect value x and replcae it with iethe r2 = x or floor(x/2):
# for each element all multiplication operations performed on it must occu before any division operations performed on it.
# Return the minimum number of operations needed so that some subset of teh resulting array has a sum exactly equal to sum. If it is impossible, return -1. 
# The floor() function returns the integer part of the division


from streamlit import cache


class solution:
    def minOperations(self, nums: List[int], sum: int) -> int:
        N = len(nums)
        INF = 10 ** 20


        @cache
        #index -> N
        # left -> 0 to sum, how many operations needed to get left sum from index to N
        def f(index, left):
            if index == N:
                if left == 0:
                    return 0
                return INF

            best = INF

            best = min(best, f(index + 1, left))
            x = nums[index]
            count = 0

            while x <= left:
                best = min(best, f(index + 1, left - x) + count)
                x += 2
                count += 1

            x = nums[index] // 2

            while x > 0:
                if left >= x:
                    best = min(best, f(index + 1, left - x) + count)
                x //= 2
                count += 1

            return best

        r = f(0, sum)
        f.cache_clear()
        if r == INF:
            return -1
        return r