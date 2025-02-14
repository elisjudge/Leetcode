class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        
        if left_sum == right_sum:
            return 0
        
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        
        return -1
        

s = Solution()

testcases = [
    {"nums": [1], "expected": 0},
    {"nums": [1,7,3,6,5,6], "expected": 3},
    {"nums": [1,2,3], "expected": -1},
    {"nums": [2,1,-1], "expected": 0}
]

for i, testcase in enumerate(testcases):
    output = s.pivotIndex(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    