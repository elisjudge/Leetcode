class Solution:
    def __init__(self) -> None:
        pass
    
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+= 1
            r-=1
        


s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]

s = Solution()
s.reverseString(s2)
