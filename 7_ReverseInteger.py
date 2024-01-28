class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x //= -1
      
        revNum = 0
        while x > 0:
            last_digit = x % 10
            revNum = revNum * 10 + last_digit
            x //= 10
        
        if revNum > (2**31 - 1):
            return 0 
        
        if negative:
            return revNum // -1

        return revNum
        
    
s = Solution()
print(s.reverse(-1234))
print(s.reverse(1534236469))

