class Solution:
    """ This solution works very well, it is quite fast but it uses
    o(n) memory because i am creating a new string"""
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1] 


class Solution2:

    """ 
    This solution will not use extra memory, but will use two
    pointers instead to check each character starting from the left
    and the right only to meet in the middle.

    I will also show a way to check alphanum without an inbuilt function
    """

    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            # Need to make sure that pointer moves when non-alphanum char
            # is encountered.
            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True


    def alphaNum(self, c: str) -> bool:
        """
        Check asci value to see if alphanum
        """
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

Sol = Solution()
Sol2 = Solution2()


print("Solution 1")
print(f'str1 = {Sol.isPalindrome(s1)}')
print(f'str2 = {Sol.isPalindrome(s2)}')
print(f'str3 = {Sol.isPalindrome(s3)}')
print()
print("Solution 2")
print(f'str1 = {Sol2.isPalindrome(s1)}')
print(f'str2 = {Sol2.isPalindrome(s2)}')
print(f'str3 = {Sol2.isPalindrome(s3)}')
print()