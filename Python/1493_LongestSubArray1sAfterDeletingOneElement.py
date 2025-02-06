class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = r = 0
        deleted = False
        max_count = 0

        while r < len(nums):
            if nums[r]:
                r += 1
            else:
                if not deleted:
                    deleted = True
                    r += 1
                else:
                    while deleted:
                        if not nums[l]:
                            deleted = False
                        l += 1
            max_count = max(max_count, (r - l))
        
        return max_count - 1

s = Solution()

testcases = [
    {"nums": [1,1,0,1], "expected": 3},
    {"nums": [0,1,1,1,0,1,1,0,1], "expected": 5},
    {"nums": [1,1,1], "expected": 2}, 
]

for i, testcase in enumerate(testcases):
    output = s.longestSubarray(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")  