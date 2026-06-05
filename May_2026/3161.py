# There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

# You are given a 2D array queries, which contains two types of queries:

# For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
# For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
# Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

# ─────────────────────────────────────────────────────────────────────────────
# APPROACH
# ─────────────────────────────────────────────────────────────────────────────
# The block fits if there is a gap of size >= sz somewhere in [0, x].
# Two kinds of gaps to check:
#   1. "Right boundary gap":  x  - (last obstacle <= x)
#      This gap hugs the right wall and is NOT stored in the tree — computed on the fly.
#   2. "Interior gaps":  every space between two consecutive obstacles, both <= x.
#      We store these in a prefix-max segment tree so we can answer in O(log N).
#
# DATA STRUCTURES
#   • SortedList  — keeps obstacles sorted so we can find prev/next in O(log N).
#   • Segment tree (max, prefix-max) — tree[p] = gap that *ends* at obstacle p
#                                      (i.e. p minus its left neighbor).
#     Querying max over [0, prev] gives the largest interior gap fully inside [0, prev].
#
# INSERTION of obstacle at x (type-1 query):
#   Let prev = largest obstacle < x,  next = smallest obstacle > x.
#   Before insertion the gap [prev, next] was recorded at position `next` as next-prev.
#   After insertion:
#     • gap ending at x    = x - prev   → update(x, x - prev)
#     • gap ending at next = next - x   → update(next, next - x)   (shrinks)
#
# TYPE-2 QUERY  [2, x, sz]:
#   prev       = last obstacle <= x
#   right_gap  = x - prev                       (boundary gap)
#   inner_max  = query(0, prev)                 (best interior gap)
#   answer     = max(right_gap, inner_max) >= sz
# ─────────────────────────────────────────────────────────────────────────────

from sortedcontainers import SortedList
from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        # ── Segment tree (iterative, max) ──────────────────────────────────
        MAX = 5 * 10**4 + 1          # positions 0 … 50 000
        tree = [0] * (2 * MAX)       # leaves at indices [MAX … 2*MAX-1]

        def update(pos: int, val: int) -> None:
            # Step 1: go to the leaf for this position
            i = pos + MAX
            tree[i] = val
            # Step 2: bubble up, each parent = max of its two children
            i >>= 1
            while i >= 1:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        def query(l: int, r: int) -> int:
            # Returns max value in positions [l, r] inclusive
            res = 0
            l += MAX
            r += MAX + 1          # make r exclusive
            while l < r:
                if l & 1:         # l is a right child → include it, move right
                    res = max(res, tree[l])
                    l += 1
                if r & 1:         # r-1 is a right child → include it, move left
                    r -= 1
                    res = max(res, tree[r])
                l >>= 1
                r >>= 1
            return res

        # ── Sorted obstacle set (sentinel 0 = origin wall) ────────────────
        # We treat 0 as a permanent obstacle/wall so every gap has a left anchor.
        obstacles = SortedList([0])
        results = []

        for q in queries:

            if q[0] == 1:
                # ── Type-1: insert obstacle at x ──────────────────────────
                x = q[1]

                # Find neighbors BEFORE inserting x
                idx      = obstacles.bisect_left(x)   # insertion point (x not in list yet)
                prev     = obstacles[idx - 1]          # largest obstacle < x
                next_obs = obstacles[idx] if idx < len(obstacles) else None

                obstacles.add(x)

                # New gap ending at x
                update(x, x - prev)

                # Shrink the gap that used to end at next_obs
                if next_obs is not None:
                    update(next_obs, next_obs - x)

            else:
                # ── Type-2: can we fit a block of size sz in [0, x]? ──────
                x, sz = q[1], q[2]

                # Last obstacle at or before x
                prev = obstacles[obstacles.bisect_right(x) - 1]

                # Gap between prev and the right boundary x
                right_gap = x - prev

                # Best gap entirely within [0, prev] (stored in segment tree)
                inner_max = query(0, prev)

                results.append(max(right_gap, inner_max) >= sz)

        return results


# ─────────────────────────────────────────────────────────────────────────────
# WORKED EXAMPLE
# queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
#
# After [1,2]: obstacles = {0, 2},  tree: gap[2]=2
# [2,3,3]: prev=2, right_gap=3-2=1, inner_max=query(0,2)=2 → max=2 < 3 → False
# [2,3,1]: prev=2, right_gap=1,     inner_max=2            → max=2 >= 1 → True
# [2,2,2]: prev=2, right_gap=0,     inner_max=query(0,2)=2 → max=2 >= 2 → True
# result = [False, True, True]  ✓
# ─────────────────────────────────────────────────────────────────────────────
