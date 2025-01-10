class Solution:
    def myAtoi(self, s: str) -> int:
        signed = False
        negative = False
        first_digit = False
        res = ""

        for char in s:
            if not first_digit and not signed:
                if char == " ":
                    continue
                elif char == "-" or char == "+":
                    signed = True
                    if char == "-":
                        negative = True
                elif 48 <= ord(char) <= 57:
                    first_digit = True
                    res += char
                else:
                    break
            else:
                if ord(char) < 48 or ord(char) > 57 :
                    break
                else:
                    res += char

        if len(res) == 0:
            return 0
        
        res = int(res) 
        if negative:
            res //= -1
            if res < (-2**31):
                res = (-2**31)
        else:
            if res > (2**31 - 1):
                res = (2**31 - 1)
        
        return res

s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("  -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("+1"))
print(s.myAtoi("+-12"))