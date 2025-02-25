class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res = []

        for s in spells:
            l, r = 0, len(potions) - 1
            idx = len(potions)

            while l <= r:
                m = l + (r - l) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            res.append(len(potions) - idx)

        return res

s = Solution()

testcases = [
    {"spells": [5,1,3], "potions": [1,2,3,4,5], "success": 7, "expected": [4,0,3]},
    {"spells": [3,1,2], "potions": [8,5,8], "success": 16, "expected": [2,0,2]}
]

for i, testcase in enumerate(testcases):
    output = s.successfulPairs(testcase["spells"], testcase["potions"], testcase["success"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   
