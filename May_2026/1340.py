# Given an array of integers arr and an integer d. In one step you can jump from index i to index:

# i + x where: i + x < arr.length and  0 < x <= d.
# i - x where: i - x >= 0 and  0 < x <= d.
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

# You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

# Notice that you can not jump outside of the array at any time.

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n

        for i in sorted(range(n), key=lambda x: arr[x]):
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] <= arr[j]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)

            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[i] <= arr[j]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
