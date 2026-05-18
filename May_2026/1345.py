# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.


from narwhals import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        visited = set()
        queue = [(0, 0)]
        value_to_indices = {}

        for i, value in enumerate(arr):
            if value not in value_to_indices:
                value_to_indices[value] = []
            value_to_indices[value].append(i)

        while queue:
            index, steps = queue.pop(0)

            if index == len(arr) - 1:
                return steps

            visited.add(index)

            for next_index in [index + 1, index - 1] + value_to_indices.get(arr[index], []):
                if 0 <= next_index < len(arr) and next_index not in visited:
                    queue.append((next_index, steps + 1))

            value_to_indices[arr[index]] = []

        return -1