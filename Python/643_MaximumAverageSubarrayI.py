class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / len(nums)
        
        running_sum = sum(nums[:k])
        max_avg = running_sum / k
        

        for r in range(k, len(nums)):
            running_sum += nums[r] - nums[r - k]
            max_avg = max(max_avg, running_sum / k)

        return max_avg

s = Solution()

testcases = [
    {"nums": [1,12,-5,-6,50,3], "k": 4, "expected": 12.75000},
    {"nums": [5], "k": 1, "expected": 5.00000}
]

for i, testcase in enumerate(testcases):
    output = s.findMaxAverage(testcase["nums"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")