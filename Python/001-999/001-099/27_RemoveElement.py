class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k

s= Solution()

testcases = [
    {"nums": [3,2,2,3], "val": 3, "expected": 2},
    {"nums": [0,1,2,2,3,0,4,2], "val": 2, "expected": 5}
]

for i, testcase in enumerate(testcases):
    output = s.removeElement(testcase["nums"], testcase["val"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")