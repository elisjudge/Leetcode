class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = [False] * len(candies)
        for kid, candies in enumerate(candies):
            if candies + extraCandies >= max_candies:
                result[kid] = True
        return result

s = Solution()

testcases = [
    {"candies": [2,3,5,1,3], "extraCandies": 3, "expected": [True,True,True,False,True]},
    {"candies": [4,2,1,1,2], "extraCandies": 1, "expected": [True,False,False,False,False]},
    {"candies": [12,1,12], "extraCandies": 10, "expected": [True,False,True]}
]

for i, testcase in enumerate(testcases):
    output = s.kidsWithCandies(testcase["candies"], testcase["extraCandies"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
        