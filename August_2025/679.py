class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6


        def dfs(nums):
            if len(nums) == 1:
                return math.isclose(nums[0], 24, abs_tol=EPS)

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        next_nums = [nums[k] for k in range(n) if k != i and k != j]

                        for val in compute(nums[i], nums[j]):
                            if dfs(next_nums + [val]):
                                return True

            return False
        

        def compute(a, b):
            results = [a + b, a - b, b - a, a * b]
            if abs(b) > 1e-6:
                results.append(a / b)
            if abs(a) > 1e-6:
                results.append(b / a)
            return results

        return dfs([float(c) for c in cards])

        