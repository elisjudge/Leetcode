import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while len(nums) >= 2:
            if nums[0] < k:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
                new_val = min(x, y) * 2 + max(x, y)
                heapq.heappush(nums, new_val)
                operations += 1
            else:
                break

        return operations


s= Solution()

testcases = [
    {"nums": [2,11,10,1,3], "k": 10, "expected": 2},
    {"nums": [1,1,2,4,9], "k": 20, "expected": 4}
]

for i, testcase in enumerate(testcases):
    output = s.minOperations(testcase["nums"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   