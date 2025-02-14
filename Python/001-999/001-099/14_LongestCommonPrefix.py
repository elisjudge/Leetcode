class Solution:
    def __init__(self) -> None:
        pass
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            
        return res

s= Solution()

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(s.longestCommonPrefix(strs1))
print(s.longestCommonPrefix(strs2))