class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if (m - 1 >= 0 and
                arr[m - 1] < arr[m] and 
                arr[m + 1] < arr[m]):
                    return m
            
            elif arr[m + 1] > arr[m]:
                l = m + 1
            
            elif arr[m - 1] > arr[m]:
                r = m - 1

s= Solution()

testcases = [
    {"arr": [0,1,0], "expected": 1},
    {"arr": [0,2,1,0], "expected": 1},
    {"arr": [0,10,5,2,0], "expected": 1},
    {"arr": [0,10,5,2], "expected": 1}
]

for i, testcase in enumerate(testcases):
    output = s.peakIndexInMountainArray(testcase["arr"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    