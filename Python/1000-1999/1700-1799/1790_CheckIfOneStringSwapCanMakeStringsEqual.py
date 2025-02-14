from collections import defaultdict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s2_chars = set(s2)
        s1_char_counts = defaultdict(int)
        s2_char_counts = defaultdict(int)
        
        char_diffs = 0
        for i in range(len(s1)):
            if s1[i] not in s2_chars:
                return False
            
            if s1[i] != s2[i]:
                char_diffs += 1
            
            s1_char_counts[s1[i]] += 1
            s2_char_counts[s2[i]] += 1
        
        return char_diffs == 2 and s1_char_counts == s2_char_counts

s = Solution()

testcases = [
    {"s1": "bankb", "s2": "kannb", "expected": False},
    {"s1": "aaa", "s2": "aaz", "expected": False},
    {"s1": "caa", "s2": "aaz", "expected": False},
    {"s1": "bank", "s2": "kanb", "expected": True},
    {"s1": "bang", "s2": "bank", "expected": False},
    {"s1": "attack", "s2": "defend", "expected": False},
    {"s1": "kelb", "s2": "kelb", "expected": True}
]

for i, testcase in enumerate(testcases):
    output = s.areAlmostEqual(testcase["s1"], testcase["s2"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")