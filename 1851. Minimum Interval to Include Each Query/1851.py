import heapq

class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

        intervals.sort(key=lambda i: i[0])
        result = {}
        heap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                interval_start, interval_end = intervals[i]
                heapq.heappush(heap, (interval_end - interval_start + 1, interval_end))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            result[q] = heap[0][0] if heap else -1
        return [result[q] for q in queries]


solution = Solution()

# Example 1
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
print("Input: intervals =", intervals, ", queries =", queries)
print("Output:", solution.minInterval(intervals, queries))
