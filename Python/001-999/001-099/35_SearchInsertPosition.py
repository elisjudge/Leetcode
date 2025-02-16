class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if target > nums[r]:
            return r+1
        elif target < nums[l]:
            return l

        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            
        return l

s = Solution()

testcases = [
    {"nums": [1,3,5,6], "target": 5, "expected": 2},
    {"nums": [1,3,5,6], "target": 2, "expected": 1},
    {"nums": [1,3,5,6], "target": 7, "expected": 4},
]

for i, testcase in enumerate(testcases):
    output = s.searchInsert(testcase["nums"], testcase["target"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   

