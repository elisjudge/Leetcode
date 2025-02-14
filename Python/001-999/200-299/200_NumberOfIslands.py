from collections import deque

class UnionFind:
    def __init__(self):
        self.roots = {}
        self.ranks = {}

    def find(self, pos:tuple):
        if pos not in self.roots:
            self.roots[pos] = pos
            self.ranks[pos] = 1
            return pos
        else:
            res = pos
            path = set()
            while res != self.roots[res]:
                path.add(res)
                res = self.roots[res]
            
            for node in path:
                self.roots[node] = res

            return res
    
    def union(self, pos1:tuple, pos2:tuple):
        r1, r2 = self.find(pos1), self.find(pos2)
        if r1 != r2:
            if self.ranks[r1] >= self.ranks[r2]:
                self.roots[r2] = r1
                self.ranks[r1] += self.ranks[r2]
            else:
                self.roots[r1] = r2
                self.ranks[r2] += self.ranks[r1]


class Solution:
    def numIslandsBFS(self, grid: list[list[str]]) -> int:
        """ Uses BFS Algorithm """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  #below, above, right, left

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                            q.append((r, c))
                            visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands

    def numIslandsDFS(self, grid: list[list[str]]) -> int:
        """ Uses the DFS algorithm """
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or 
                r >= rows or
                c < 0 or
                c >= cols or
                grid[r][c] != "1"):
                    return
            else:
                grid[r][c] = "0"
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r - 1, c)


        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
                    

    def numIslandsUnion(self, grid: list[list[str]]) -> int:
        """ Uses the Union Find algorithm """
        uf = UnionFind()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    _ = uf.find((r, c))
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if (x, y) in uf.roots:
                            uf.union((r, c), (x, y))
        
        return len(set([uf.find(root) for root in uf.roots.values()]))


s = Solution()

testcases = [
    {
        "grid": [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]], 
        "expected": 1
    },
    {
        "grid": [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]], 
        "expected": 3
    }
]

for i, testcase in enumerate(testcases):
    outputBFS = s.numIslandsBFS(testcase["grid"])
    outputUnion = s.numIslandsUnion(testcase["grid"])
    outputDFS = s.numIslandsDFS(testcase["grid"])

    if outputBFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(BFS): {outputBFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(BFS): {outputBFS}")
    
    if outputDFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(DFS): {outputDFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(DFS): {outputDFS}")
    
    if outputUnion == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(Union Find): {outputUnion}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(Union Find): {outputUnion}")
