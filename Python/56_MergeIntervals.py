class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = output[-1][1]

            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])
        return output
    
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]

print(s.merge(intervals))
print(s.merge(intervals2))