class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2        
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1



s = Solution()

testcases = [
    {"nums": [4,5,6,7,0,1,2], "target": 0, "expected": 4},
    {"nums": [4,5,6,7,0,1,2], "target": 3, "expected": -1},
    {"nums": [3,4,5,6,1,2], "target": 1, "expected": 4},
    {"nums": [3,5,6,0,1,2], "target": 4, "expected": -1},
    {"nums": [1], "target": 0, "expected": -1}
]

for i, testcase in enumerate(testcases):
    output = s.search(testcase["nums"], testcase["target"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    