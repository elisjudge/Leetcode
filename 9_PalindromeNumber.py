class Solution:
    def intToStringList(self, x: int) -> list:
        return [digit for digit in str(x)]
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True       
        
        x_str = self.intToStringList(x)
        l = 0
        r = len(x_str) - 1

        while l < r:
            if x_str[l] != x_str[r]:
                return False
            l+= 1
            r-= 1

        return True

s = Solution()
print("String Solution")
print(f"231: {s.isPalindrome(231)}")
print(f"121: {s.isPalindrome(121)}")
print(f"-121: {s.isPalindrome(-121)}")
print(f"10: {s.isPalindrome(10)}")
print(f"11: {s.isPalindrome(11)}")
print(f"8: {s.isPalindrome(8)}")

class Solution_Integer:
    def countNumDigits(self, x:int) -> int:
        count = 0
        while x != 0:
            x //= 10
            count += 1
        return count
    
    def getNthDigit(self, x:int, n:int) -> int:
        """ Gets nth digit from right to left"""
        return x // 10**n % 10

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        l = self.countNumDigits(x) - 1
        r = 0

        while l > r:
            left_digit = self.getNthDigit(x, l)
            right_digit = self.getNthDigit(x, r)

            if left_digit != right_digit:
                return False
            l -= 1
            r += 1
        
        return True

print()

s_int = Solution_Integer()
print("Integer Only Solution")
print(f"231: {s_int.isPalindrome(231)}")
print(f"121: {s_int.isPalindrome(121)}")
print(f"-121: {s_int.isPalindrome(-121)}")
print(f"10: {s_int.isPalindrome(10)}")
print(f"11: {s_int.isPalindrome(11)}")
print(f"8: {s_int.isPalindrome(8)}")