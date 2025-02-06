class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

s = Solution()

testcases = [
    {
        "s": "leet**cod*e", 
        "expected": "lecoe"
    },
    {
        "s": "erase*****", 
        "expected": ""
    }
]

for i, testcase in enumerate(testcases):
    output = s.removeStars(testcase["s"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")