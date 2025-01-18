class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        trapped_water = 0

        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                trapped_water += left_max - height[l]
            elif left_max > right_max:
                r -= 1
                right_max = max(right_max, height[r])
                trapped_water += right_max - height[r]
        
        return trapped_water

s = Solution()

testcases = [
    {"height": [0,1,0,2,1,0,1,3,2,1,2,1], "expected": 6},
    {"height": [4,2,0,3,2,5], "expected": 9},
    {"height": [0,2,0,3,1,0,1,3,2,1], "expected": 9}
]

for i, testcase in enumerate(testcases):
    output = s.trap(testcase["height"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")