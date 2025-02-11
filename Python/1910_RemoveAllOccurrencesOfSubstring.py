class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)

            if len(stack) < part_length:
                continue

            if "".join(stack[len(stack) - part_length:]) == part:
                for _ in range(part_length):
                    stack.pop()
        
        return "".join(stack)

s = Solution()

testcases = [
    {"s": "daabcbaabcbc", "part": "abc", "expected": "dab"},
    {"s": "axxxxyyyyb", "part": "xy", "expected": "ab"},
    {"s": "ax", "part": "axx", "expected": "ax"},
    {"s": "axexeexxxxxxxxxexxexxxxxxxxxy", "part": "x", "expected": "aeeeeey"}
]

for i, testcase in enumerate(testcases):
    output = s.removeOccurrences(testcase["s"], testcase["part"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")