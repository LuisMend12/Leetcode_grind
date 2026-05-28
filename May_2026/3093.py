# You are given two arrays of strings wordsContainer and wordsQuery.

# For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

# Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Trie on reversed strings; each node stores the best container index
        # (smallest length word, earlier index for ties)
        trie = [{}]
        best = [-1]

        def insert(word, idx):
            node = 0
            if best[node] == -1 or len(word) < len(wordsContainer[best[node]]):
                best[node] = idx
            for ch in reversed(word):
                if ch not in trie[node]:
                    trie.append({})
                    best.append(-1)
                    trie[node][ch] = len(trie) - 1
                node = trie[node][ch]
                if best[node] == -1 or len(word) < len(wordsContainer[best[node]]):
                    best[node] = idx

        for i, word in enumerate(wordsContainer):
            insert(word, i)

        def query(word):
            node = 0
            for ch in reversed(word):
                if ch not in trie[node]:
                    break
                node = trie[node][ch]
            return best[node]

        return [query(q) for q in wordsQuery]
