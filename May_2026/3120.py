# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.



class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()

        for char in word:
            if char.islower():
                lowercase.add(char)
            else:
                uppercase.add(char.lower())

        return len(lowercase.intersection(uppercase))