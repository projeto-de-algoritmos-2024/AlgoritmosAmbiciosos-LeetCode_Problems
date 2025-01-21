from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        end = intervals[0][1]
        count = len(intervals) - 1

        for i in range(1, len(intervals)):
            
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count -= 1

        return count

solution = Solution()

# Example 1
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print("Input: intervals =", intervals)
print("Output:", solution.eraseOverlapIntervals(intervals))  

# Example 2
intervals = [[1, 2], [1, 2], [1, 2]]
print("\nInput: intervals =", intervals)
print("Output:", solution.eraseOverlapIntervals(intervals))  

# Example 3
intervals = [[1, 2], [2, 3]]
print("\nInput: intervals =", intervals)
print("Output:", solution.eraseOverlapIntervals(intervals))
