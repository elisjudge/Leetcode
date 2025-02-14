class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_alt = 0 + gain[0]
        max_alt = max(0, curr_alt)
        
        for i in range(1, len(gain)):
            curr_alt = curr_alt + gain[i]
            max_alt = max(max_alt, curr_alt)
        
        return max_alt

s= Solution()

testcases = [
    {"gain": [-5,1,5,0,-7], "expected": 1},
    {"gain": [-5], "expected": 0},
    {"gain": [-5, 6], "expected": 1},
    {"gain": [-4,-3,-2,-1,4,3,2], "expected": 0}
]

for i, testcase in enumerate(testcases):
    output = s.largestAltitude(testcase["gain"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    