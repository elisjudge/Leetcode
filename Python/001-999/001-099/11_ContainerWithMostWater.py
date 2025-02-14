class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            width = r - l   
            h = min(height[l], height[r])
            area = width * h

            max_area = max(area, max_area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area

s= Solution()

testcases = [
    {"height": [1,8,6,2,5,4,8,3,7], "expected": 49},
    {"height": [1,1], "expected": 1}
]

for i, testcase in enumerate(testcases):
    output = s.maxArea(testcase["height"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")