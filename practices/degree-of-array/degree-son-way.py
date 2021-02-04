from math import inf


class Solution:
    def findShortestArray(self, nums):
        cmap = {}
        min_subarray = inf

        for i, num in enumerate(nums):
            if num not in cmap:
                cmap[num] = [i]
            else:
                cmap[num].append(i)

        degree = max([len(c) for c in cmap.values()])

        for value in cmap.values():
            if len(value) == degree:
                subarray = value[-1]-value[0]

                if subarray < min_subarray:
                    min_subarray = subarray

        return min_subarray+1


Solution.findShortestArray(Solution, [1, 2, 2, 3, 1, 3, 3, 3, 1, 3])
