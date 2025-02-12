class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) if k >= len(nums) else k

        def reverse_array_in_place(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        operations = [(0, len(nums) - 1), (0, k - 1), (k, len(nums) - 1)]

        for operation in operations:
            l, r = operation
            reverse_array_in_place(nums, l, r)

s = Solution()

testcases = [
    {"nums": [-1], "k": 2, "expected": [-1]},
    {"nums": [1,2,3,4,5,6,7], "k": 10, "expected": [5,6,7,1,2,3,4]},
    {"nums": [1,2,3,4,5,6,7], "k": 8, "expected": [7,1,2,3,4,5,6]},
    {"nums": [1,2,3,4,5,6,7], "k": 7, "expected": [1,2,3,4,5,6,7]},
    {"nums": [1,2,3,4,5,6,7], "k": 3, "expected": [5,6,7,1,2,3,4]},
    {"nums": [-1,-100,3,99], "k": 2, "expected": [3,99,-1,-100]},
]

for i, testcase in enumerate(testcases):
    output = testcase["nums"]
    s.rotate(output, testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")  