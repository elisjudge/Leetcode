class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) > len(haystack) or 
            len(needle) == 0):
                return -1
        
        if needle == haystack:
            return 0

        l = 0
        for r in range(len(needle), len(haystack) + 1):
            if haystack[l:r] == needle:
                return l
            l += 1
        
        return - 1
            
s = Solution()

testcases = [
    {"haystack": "sadbutsad", "needle": "sad", "expected": 0},
    {"haystack": "leetcode", "needle": "leeto", "expected": -1},
    {"haystack": "a", "needle": "a", "expected": 0},
    {"haystack": "abc", "needle": "c", "expected": 2},
]

for i, testcase in enumerate(testcases):
    output = s.strStr(testcase["haystack"],testcase["needle"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")      