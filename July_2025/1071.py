class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd

        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = gcd(len(str1), len(str2))

        return str1[:gcd_len]