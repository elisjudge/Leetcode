class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = nums[0]
        result = max_sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                max_sum += nums[i]
            else:
                max_sum = nums[i]
            
            result = max(result, max_sum)          

        return result  

s= Solution()

testcases = [
    {"nums": [10,20,30,5,10,50], "expected": 65},
    {"nums": [10,20,30,40,50], "expected": 150}, 
    {"nums": [12,17,15,13,10,11,12], "expected": 33}
]

for i, testcase in enumerate(testcases):
    output = s.maxAscendingSum(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")  
