class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = r = 0
        max_count = 0
        lookahead_count = 0

        while r < len(nums):
            if nums[r]:
                r += 1
            else:
                if lookahead_count < k:
                    lookahead_count += 1
                    r += 1
                else:
                    while lookahead_count == k:
                        if not nums[l]:
                            lookahead_count -= 1 
                        l += 1
            max_count = max(max_count, (r - l))
        return max_count

s = Solution()

testcases = [
    {"nums": [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], "k": 3, "expected": 10},
    {"nums": [1,1,1,0,0,0,1,1,1,1,0], "k": 2, "expected": 6},
]

for i, testcase in enumerate(testcases):
    output = s.longestOnes(testcase["nums"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")