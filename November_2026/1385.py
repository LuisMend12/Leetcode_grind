class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def found(x):
            for y in arr2:
                if abs(x - y) <= d:
                    return True
            return False
        
        count = 0
        for x in arr1:
            if not found(x):

                count += 1
        return count

    