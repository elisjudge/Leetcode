class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_n, close_n):
            if open_n == close_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()
            
            if close_n < open_n:
                stack.append(")")
                backtrack(open_n, close_n + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

s = Solution()

testcases = [
    {"n": 2, "expected": ["(())","()()"]},
    {"n": 3, "expected": ["((()))","(()())","(())()","()(())","()()()"]},
    {"n": 1, "expected": ["()"]}
]

for i, testcase in enumerate(testcases):
    output = s.generateParenthesis(testcase["n"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")