class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_count = [0] * 26

        for char in s[:k]:
            idx = ord(char) - ord('a')
            window_count[idx] += 1
        
        max_count = (window_count[ord("a") - ord('a')] +
                    window_count[ord("e") - ord('a')] +
                    window_count[ord("i") - ord('a')] +
                    window_count[ord("o") - ord('a')] +
                    window_count[ord("u") - ord('a')]) 
        
        for i in range(k, len(s)):
            window_count[ord(s[i]) - ord('a')] += 1
            window_count[ord(s[i - k]) - ord('a')] -= 1
            max_count = max(
                max_count, 
                (window_count[ord("a") - ord('a')] +
                window_count[ord("e") - ord('a')] +
                window_count[ord("i") - ord('a')] +
                window_count[ord("o") - ord('a')] +
                window_count[ord("u") - ord('a')])) 

        return max_count

s = Solution()

testcases = [
    {"s": "abciiidef", "k": 3, "expected": 3},
    {"s": "aeiou", "k": 2, "expected": 2},
    {"s": "leetcode", "k": 3, "expected": 2},
]

for i, testcase in enumerate(testcases):
    output = s.maxVowels(testcase["s"], testcase["k"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")