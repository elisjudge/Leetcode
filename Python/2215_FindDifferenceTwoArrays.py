class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        num1_set = set(nums1)
        num2_set = set(nums2)

        nums1_unique = list(num1_set - num2_set)
        nums2_unique = list(num2_set - num1_set)

        return [nums1_unique, nums2_unique]

s = Solution()

testcases = [
    {"nums1": [1,2,3], "nums2": [2,4,6], "expected": [[1,3],[4,6]]},
    {"nums1": [1,2,3,3], "nums2": [1,1,2,2], "expected": [[3],[]]}
]

for i, testcase in enumerate(testcases):
    output = s.findDifference(testcase["nums1"], testcase["nums2"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")