class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        while l <= r:
            m = (l + r) // 2
            
            if letters[m] == target:
                while m < len(letters) and letters[m] == target:
                    m += 1
                return letters[m] if m < len(letters) else letters[0]
            
            elif ord(letters[m]) > ord(target):
                r = m - 1

            elif ord(letters[m]) < ord(target):
                l = m + 1

        if r < 0 or l >= len(letters):
            return letters[0]
        else:
            return letters[l]
            

s = Solution()

testcases = [
    {"letters": ["c","f","j"], "target": "c", "expected": "f"},
    {"letters": ["c","f","j"], "target": "a", "expected": "c"},
    {"letters": ["x","x","y","y"], "target": "z", "expected": "x"}
]

for i, testcase in enumerate(testcases):
    output = s.nextGreatestLetter(testcase["letters"], testcase["target"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    