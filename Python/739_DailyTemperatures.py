class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append((idx, temp))

        return result

s = Solution()

testcases = [
    {"temperatures": [73,74,75,71,69,72,76,73], "expected": [1,1,4,2,1,1,0,0]},
    {"temperatures": [30,40,50,60], "expected": [1,1,1,0]},
    {"temperatures": [30,60,90], "expected": [1,1,0]}
]

for i, testcase in enumerate(testcases):
    output = s.dailyTemperatures(testcase["temperatures"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   