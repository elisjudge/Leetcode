class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        
        if n == 1:
            return True
        
        dips = 0
        if nums[-1] > nums[0]:
            dips += 1
        

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                dips += 1

        return dips <= 1


s = Solution()

testcases = [
    {"nums": [3,4,5,1,2], "expected": True},
    {"nums": [2,1,3,4], "expected": False},
    {"nums": [1,2,3], "expected": True},
    {"nums": [1,1,1], "expected": True},
]

for i, testcase in enumerate(testcases):
    output = s.check(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}") 