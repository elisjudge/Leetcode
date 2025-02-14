class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

s = Solution()

testCases = [
    {"flowerbed": [1,0,0,0,1], "n": 1, "expected": True},
    {"flowerbed": [1,0,0,0,1], "n": 2, "expected": False},
    {"flowerbed": [0,0,0], "n": 2, "expected": True},
    {"flowerbed": [0,0,0], "n": 3, "expected": False},
    {"flowerbed": [0,0,1], "n": 1, "expected": True},
    {"flowerbed": [1,0,0], "n": 1, "expected": True},
    {"flowerbed": [0,0,1], "n": 2, "expected": False},
    {"flowerbed": [0,1], "n": 1, "expected": False},
    {"flowerbed": [0,0], "n": 2, "expected": False},
    {"flowerbed": [0,0], "n": 1, "expected": True},
]

for i, testcase in enumerate(testCases):
    output = s.canPlaceFlowers(testcase["flowerbed"], testcase["n"])
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")



