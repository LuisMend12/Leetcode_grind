# You are given two integers num1 and num2 representing an inclusive range [num1, num2].

# The waviness of a number is defined as the total count of its peaks and valleys:

# A digit is a peak if it is strictly greater than both of its immediate neighbors.
# A digit is a valley if it is strictly less than both of its immediate neighbors.
# The first and last digits of a number cannot be peaks or valleys.
# Any number with fewer than 3 digits has a waviness of 0.
# Return the total sum of waviness for all numbers in the range [num1, num2].
from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self._upto(num2) - self._upto(num1 - 1)

    def _upto(self, N: int) -> int:
        # Sum of waviness for all numbers in [0, N].
        if N < 0:
            return 0
        digits = list(map(int, str(N)))
        n = len(digits)

        # State: position i, the two previous real digits (prev2, prev1; -1 = none yet),
        # whether the number has started (a nonzero digit seen), and the tight flag.
        # Returns (count of numbers, total waviness) for the suffix.
        @lru_cache(maxsize=None)
        def dp(i, prev2, prev1, started, tight):
            if i == n:
                return (1, 0)
            limit = digits[i] if tight else 9
            tot_cnt = 0
            tot_wav = 0
            for cur in range(limit + 1):
                ntight = tight and (cur == limit)
                nstarted = started or (cur > 0)
                contrib = 0
                if not nstarted:                       # still in leading zeros
                    np2, np1 = -1, -1
                elif not started:                      # first real digit
                    np2, np1 = -1, cur
                else:
                    # prev1 is the middle of the triple (prev2, prev1, cur).
                    if prev2 != -1 and prev1 != -1 and (
                        (prev1 > prev2 and prev1 > cur) or (prev1 < prev2 and prev1 < cur)
                    ):
                        contrib = 1
                    np2, np1 = prev1, cur
                sub_cnt, sub_wav = dp(i + 1, np2, np1, nstarted, ntight)
                tot_cnt += sub_cnt
                tot_wav += sub_wav + contrib * sub_cnt
            return (tot_cnt, tot_wav)

        result = dp(0, -1, -1, False, True)[1]
        dp.cache_clear()
        return result
