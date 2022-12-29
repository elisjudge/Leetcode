class Solution:
    def __init__(self) -> None:
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

s = Solution()

tests = [["anagram", "nagaram"], ["rat","car"]]

for test in tests:
    print(s.isAnagram(test[0], test[1]))