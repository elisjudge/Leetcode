class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1 or k == min(nums):
            return 0
        
        nums.sort()
        l, r = 0, len(nums) - 1
        operations = 0
        while l < r:
            if nums[l] + nums[r] == k:
                operations += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                if nums[l] == nums[l + 1]:
                    while nums[l] == nums[l + 1]:
                        l += 1
                else:
                    l += 1

            elif nums[l] + nums[r] > k:
                if nums[r] == nums[r - 1]:
                    while nums[r] == nums[r - 1]:
                        r -= 1
                else:
                    r -= 1
        return operations

s = Solution()

testcases = [
    {"nums": [3,5,1,5], "k": 2, "expected": 0},
    {"nums": [3,1,5,1,1,1,1,1,2,2,3,2,2], "k": 1, "expected": 0},
    {"nums": [1,2,3,4], "k": 5, "expected": 2},
    {"nums": [3,1,3,4,3], "k": 6, "expected": 1},
]

for i, testcase in enumerate(testcases):
    output = s.maxOperations(testcase["nums"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")