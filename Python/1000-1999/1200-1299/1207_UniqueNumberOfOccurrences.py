class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurences_map = {}
        unique_occurences = set()

        for num in arr:
            occurences_map[num] = 1 + occurences_map.get(num, 0)
        
        for val in occurences_map.values():
            unique_occurences.add(val)
        
        return len(occurences_map) == len(unique_occurences)


s = Solution()

testcases = [
    {"arr": [1,2,2,1,1,3], "expected": True},
    {"arr": [1,2], "expected": False},
    {"arr": [-3,0,1,-3,1,1,1,-3,10,0], "expected": True}
]

for i, testcase in enumerate(testcases):
    output = s.uniqueOccurrences(testcase["arr"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    