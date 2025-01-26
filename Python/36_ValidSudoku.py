from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols_hashmap = defaultdict(list)
        rows_hashmap = defaultdict(list)
        squares_hashmap = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board[0])):
                cell = board[row][col]
                current_square = (row // 3, col // 3)

                if cell != ".":
                    if (cell in cols_hashmap[col] or
                        cell in rows_hashmap[row] or 
                        cell in squares_hashmap[current_square]):
                            return False
                    
                    cols_hashmap[col].append(cell)
                    rows_hashmap[row].append(cell)
                    squares_hashmap[current_square].append(cell)
        return True

s = Solution()

testcases = [
    {
        "board": [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]],
        "expected": True
    },
    {
        "board": [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]], 
        "expected": False
    }
]

for i, testcase in enumerate(testcases):
    output = s.isValidSudoku(testcase["board"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   