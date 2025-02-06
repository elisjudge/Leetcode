class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2) or
            set(word1) != set(word2)):
                return False
        
        word1_hashmap = {}
        word2_hashmap = {}

        for i in range(len(word1)):
            word1_hashmap[word1[i]] = 1 + word1_hashmap.get(word1[i], 0)
            word2_hashmap[word2[i]] = 1 + word2_hashmap.get(word2[i], 0)

        if sorted(word1_hashmap.values()) == sorted(word2_hashmap.values()):
            return True
        
        return False

s = Solution()

testcases = [
    {"word1": "abbzzca", "word2": "babzzcz", "expected": False},
    {"word1": "abc", "word2": "bca", "expected": True},
    {"word1": "a", "word2": "aa", "expected": False},
    {"word1": "cabbba", "word2": "abbccc", "expected": True},
]

for i, testcase in enumerate(testcases):
    output = s.closeStrings(testcase["word1"], testcase["word2"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")