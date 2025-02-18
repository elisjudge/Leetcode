class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 1
        n = len(nums)
        k = 1

        if n == 1:
            return k

        while r < n:
            if nums[l] == nums[r]:
                r+= 1
            elif nums[l] != nums[r]:
                nums[k] = nums[r]
                k+= 1
                l = r
                r += 1
        return k

s= Solution()

testcases = [
    {"nums": [0,0,1,1,1,2,2,3,3,4], "expected": 5},
    {"nums": [1,1,2], "expected": 2}
]

for i, testcase in enumerate(testcases):
    output = s.removeDuplicates(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")