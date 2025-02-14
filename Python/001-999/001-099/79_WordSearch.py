class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        nrows, ncols = len(board), len(board[0])
        path = set()

        def dfs(row_idx, col_idx, word_idx):
            if word_idx == len(word):
                return True
            if (row_idx < 0 or
                col_idx < 0 or
                row_idx >= nrows or
                col_idx >= ncols or
                word[word_idx] != board[row_idx][col_idx] or
                (row_idx, col_idx) in path):
                    return False
            path.add((row_idx, col_idx))
            res = (dfs(row_idx + 1, col_idx, word_idx + 1) or
                   dfs(row_idx - 1, col_idx, word_idx + 1) or
                   dfs(row_idx, col_idx + 1, word_idx + 1) or
                   dfs(row_idx, col_idx - 1, word_idx + 1))
            path.remove((row_idx, col_idx))
            return res

        for row in range(nrows):
            for col in range(ncols):
                if dfs(row, col, 0): return True
        
        return False

s = Solution()

testcases = [
    {
        "board": [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]], 
        "word": "ABCCED", 
        "expected": True
    },
    {
        "board": [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]], 
        "word": "SEE", 
        "expected": True
    },
    {
        "board": [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]], 
        "word": "ABCB", 
        "expected": False
    }
]

for i, testcase in enumerate(testcases):
    output = s.exist(testcase["board"], testcase["word"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")