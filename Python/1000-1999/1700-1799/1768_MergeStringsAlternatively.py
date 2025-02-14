class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr = 0
        result = ""
        while ptr < len(word1) and ptr < len(word2):
            result += word1[ptr]
            result += word2[ptr]
            ptr += 1
        
        if ptr < len(word1):
            result += word1[ptr:]
        elif ptr < len(word2):
            result += word2[ptr:]
        return result

s = Solution()

testcases = [
    {"word1": "abc", "word2": "pqr", "expected": "apbqcr"},
    {"word1": "ab", "word2": "pqrs", "expected": "apbqrs"},
    {"word1": "abcd", "word2": "pq", "expected":"apbqcd"}
]

for i, testcase in enumerate(testcases):
    output = s.mergeAlternately(testcase["word1"], testcase["word2"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
        