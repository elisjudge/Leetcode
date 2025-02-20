class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n <= 1:
            if n == 0 or nums[0] != target:
                return [-1, -1]
            elif nums[0] == target:
                return [0, 0]
        
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            
            else:
                start = m
                end = m
                while start - 1 >= l and nums[start - 1] == target:
                    start -= 1
                while end + 1 <= r and nums[end + 1] == target:
                    end += 1

                return [start, end]
            
        return [-1, -1]



s= Solution()

testcases = [
    {"nums": [5,7,7,8,8,10], "target": 8, "expected": [3,4]},
    {"nums": [5,7,7,8,8,10], "target": 6, "expected": [-1,-1]},
    {"nums": [5,7,7,8,8,8,8,8,8], "target": 8, "expected": [3,8]},
    {"nums": [], "target": 0, "expected": [-1,-1]},
    {"nums": [1], "target": 1, "expected": [0, 0]},
    {"nums": [1,3], "target": 3, "expected": [1, 1]},
    {"nums": [3,3], "target": 3, "expected": [0, 1]},
    {"nums": [1,3], "target": 1, "expected": [0, 0]},
]

for i, testcase in enumerate(testcases):
    output = s.searchRange(testcase["nums"], testcase["target"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}") 