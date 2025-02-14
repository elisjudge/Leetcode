class Solution:
    def __init__(self) -> None:
        pass

    def validPalindrome(self, s: str) -> bool:
        """
        Uses two pointers to iterate left to right and right to left
        to check whether characters at respective ends are equal. If
        true, the pointers move inward.  

        If there is one inequality, then two slices are taken. In one
        slice the left pointer character is removed, and in the other
        the right pointer character is removed. 

        The both substrings are checked against their mirrored version
        and if the check returns true for either, then the string is
        still a valid palindrome because we are permitted to remove at 
        most one character from the string. 
        """

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or
                        skipR == skipR[::-1])
            l, r = l+1, r-1
        return True


s1 = "aba"
s2 = "abca"
s3 = "abc"

sol = Solution()

print(sol.validPalindrome(s1))
print(sol.validPalindrome(s2))
print(sol.validPalindrome(s3))


