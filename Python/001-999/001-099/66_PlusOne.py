class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits
        
s = Solution()

testcases = [
    {"digits": [1,2,3], "expected": [1,2,4]},
    {"digits": [1,2,3,4], "expected": [1,2,3,5]},
    {"digits": [9,9,9], "expected": [1,0,0,0]},
    {"digits": [4,3,2,1], "expected": [4,3,2,2]},
    {"digits": [9], "expected": [1,0]}
]

for i, testcase in enumerate(testcases):
    output = s.plusOne(testcase["digits"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")