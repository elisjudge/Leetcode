from collections import defaultdict
import heapq

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = []
        sums = defaultdict(list)

        def sum_digits(num:int) -> int:
            if num < 10:
                return num
            string_num = str(num)
            digits = list(string_num)
            digits_sum = sum([int(digit) for digit in digits])
            return digits_sum
        
        for i in range(len(nums)):
            digit_sum = sum_digits(nums[i])

            if digit_sum in sums:
                num_j =  sums[digit_sum][-1]
                heapq.heappush(max_sum, -(nums[i] + num_j))

            sums[digit_sum].append(nums[i])

        return -(heapq.heappop(max_sum)) if len(max_sum) > 0 else -1

s= Solution()

testcases = [
    {"nums": [18,43,36,13,7], "expected": 54},
    {"nums": [10,12,19,14], "expected": -1}
]

for i, testcase in enumerate(testcases):
    output = s.maximumSum(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   