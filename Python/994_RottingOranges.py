from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        nrows, ncols = len(grid), len(grid[0])
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = dr + r, dc + c
                    if (row < 0 or
                        row == nrows or
                        col < 0 or
                        col == ncols or
                        grid[row][col] != 1):
                            continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

s = Solution()

testcases = [
    {
        "grid": [
            [1,1,0],
            [0,1,1],
            [0,1,2]], 
        "expected": 4
    },
    {
        "grid": [
            [2,1,1],
            [1,1,0],
            [0,1,1]], 
        "expected": 4
    },
    {
        "grid": [
            [2,1,1],
            [0,1,1],
            [1,0,1]], 
        "expected": -1
    },
    {
        "grid": [
            [0,2]], 
        "expected": 0
    },
    {
        "grid": [
            [1,0,1],
            [0,2,0],
            [1,0,1]], 
        "expected": -1
    }
]

for i, testcase in enumerate(testcases):
    output = s.orangesRotting(testcase["grid"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(BFS): {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(BFS): {output}")
    
        