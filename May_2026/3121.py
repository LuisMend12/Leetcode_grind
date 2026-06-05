# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

# Return the number of special letters in word.


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            elif c.lower() not in first_upper:
                first_upper[c.lower()] = i

        count = 0
        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                count += 1

        return count