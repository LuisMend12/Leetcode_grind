class Solution:
    def findRotation(self, g1: List[List[int]], g2: List[List[int]]) -> bool:
        return g2 in accumulate([g1]*4,lambda g,_:[*map(list,zip(*g[::-1]))])