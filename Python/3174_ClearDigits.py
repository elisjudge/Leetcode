class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            
            elif char.isdigit():
                stack.pop()

        return "".join(stack)

s = Solution()

testcases = [
    {"s": "abc", "expected": "abc"},
    {"s": "cb34", "expected": ""}
]

for i, testcase in enumerate(testcases):
    output = s.clearDigits(testcase["s"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
