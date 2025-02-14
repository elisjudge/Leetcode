from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        diff_count = defaultdict(int)
        good_pair_count = 0
        n = len(nums)

        for i in range(n):
            diff = nums[i] - i
            if diff in diff_count:
                good_pair_count += diff_count[diff]
            
            diff_count[diff] += 1

        total_pairs = n * (n - 1) / 2
        return int(total_pairs - good_pair_count)

s= Solution()

testcases = [
    {"nums": [4,1,3,3], "expected": 5},
    {"nums": [1,2,3,4,5], "expected": 0} 
]

for i, testcase in enumerate(testcases):
    output = s.countBadPairs(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")  