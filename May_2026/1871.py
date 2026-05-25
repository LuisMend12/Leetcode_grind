# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False

        queue = [0]
        farthest = 0

        while queue:
            i = queue.pop(0)

            for j in range(max(i + minJump, farthest + 1), min(i + maxJump, n - 1) + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)

            farthest = max(farthest, i + maxJump)

        return False