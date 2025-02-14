class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if m**2 == x:
                return m
            elif m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
        return res

s = Solution()

testCases = [
    {"x": 1, "expected": 1},
    {"x": 2, "expected": 1},
    {"x": 4, "expected": 2},
    {"x": 8, "expected": 2},
    {"x": 16, "expected": 4},
    {"x": 32, "expected": 5},
    {"x": 64, "expected": 8},
    {"x": 128, "expected": 11},
    {"x": 256, "expected": 16}
]

for i, testcase in enumerate(testCases):
    output = s.mySqrt(testcase["x"])
    
    if round(output, 5) == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")