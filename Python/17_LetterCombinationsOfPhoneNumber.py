class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in keypad[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        
        return res

s = Solution()

testcases = [
    {"digits": "23", "expected": ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
    {"digits": "", "expected": []},
    {"digits": "2", "expected": ["a","b","c"]}
]

for i, testcase in enumerate(testcases):
    output = s.letterCombinations(testcase["digits"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")