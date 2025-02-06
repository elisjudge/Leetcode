class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        N = len(grid)
        if N == 1:
            return 1
        
        col_arrays = {}
        pairs = 0
           
        for col in range(N):
            col_array = [grid[i][col] for i in range(N)]
            col_arrays[tuple(col_array)] = 1 + col_arrays.get(tuple(col_array), 0)
        
        for row in grid:
            pairs += col_arrays.get(tuple(row), 0)

        return pairs 

s = Solution()

testcases = [
    {
        "grid": [[3,2,1],[1,7,6],[2,7,7]], 
        "expected": 1
    },
    {
        "grid": [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 
        "expected": 3
    },
    {
        "grid": [[1,0,1],[0,2,0],[1,0,1]], 
        "expected": 5
    }
]

for i, testcase in enumerate(testcases):
    output = s.equalPairs(testcase["grid"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")