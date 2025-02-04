class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["A", "E", "I", "O", "U"])
        result = list(s)
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l].upper() in vowels:
                while l <= r and s[r].upper() not in vowels:
                    r -= 1
                if s[r].upper() in vowels:
                    result[l], result[r] = result[r], result[l]
                    r -= 1
            l += 1

        return ''.join(result)            

s= Solution()

testcases = [
    {"s": "IceCreAm", "expected": "AceCreIm"},
    {"s": "leetcode", "expected": "leotcede"}
]

for i, testcase in enumerate(testcases):
    output = s.reverseVowels(testcase["s"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    