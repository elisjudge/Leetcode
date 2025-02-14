class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        l = 0
        r = insert_ptr = len(nums) - 1

        while l <= r:
            left_tail = nums[l] ** 2
            right_tail = nums[r] ** 2

            if left_tail >= right_tail:
                res[insert_ptr] = left_tail
                l += 1
            else:
                res[insert_ptr] = right_tail
                r -= 1
            insert_ptr -= 1

        return res
        
s = Solution()

testcases = [
    {
        "nums": [-4,-1,0,3,10],
        "expected": [0,1,9,16,100]
    },
    {
        "nums": [-12,-4,-1,0,3,10],
        "expected": [0,1,9,16,100,144]
    },
    {
        "nums": [-7,-3,2,3,11], 
        "expected": [4,9,9,49,121]
    },
    {
        "nums": [-11,-7,-3,2,3,11], 
        "expected": [4,9,9,49,121,121]
    },
]

for i, testcase in enumerate(testcases):
    output = s.sortedSquares(testcase["nums"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
    