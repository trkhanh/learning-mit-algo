class Solution:
    def findShortestSubArray(self, numbs):
        degree = 1
        degree_numbs = {numbs[0]: [1, 0]}
        result = 1
        i = 0
        for i in range(1, len(numbs)):
            if numbs[i] in degree_numbs:
                degree_numbs[numbs[i]][0] += 1
                i_degree = degree_numbs[numbs[i]][0]
                if i_degree == degree:
                    result = min(result, i - degree_numbs[numbs[i]][1] + 1)
                    degree = i_degree
                elif i_degree > degree:
                    result = i - degree_numbs[numbs[i]][1] + 1
                    degree = i_degree
            else:
                i_degree = 1
                degree_numbs[numbs[i]] = [1, i]
        return result


Solution.findShortestSubArray(Solution, [1, 2, 2, 3, 1, 3, 3, 3, 1, 3])
