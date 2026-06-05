# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

# Notice that you can not jump outside of the array at any time.


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = [start]

        while queue:
            index = queue.pop(0)

            if arr[index] == 0:
                return True

            visited.add(index)

            for next_index in [index + arr[index], index - arr[index]]:
                if 0 <= next_index < len(arr) and next_index not in visited:
                    queue.append(next_index)

        return False