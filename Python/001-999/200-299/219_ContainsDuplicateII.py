class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dups = set()
        i = 0

        for j in range(len(nums)):
            if j - i > k:
                dups.remove(nums[i])
                i += 1
            if nums[j] in dups:
                return True
            dups.add(nums[j])
        
        return False

s = Solution()

testcases = [
    {"nums": [1,2,3,1,2,3], "k": 2, "expected": False},
    {"nums": [1,2,3,1], "k": 3, "expected": True},
    {"nums": [1,0,1,1], "k": 1, "expected": True},
]

for i, testcase in enumerate(testcases):
    output = s.containsNearbyDuplicate(testcase["nums"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")