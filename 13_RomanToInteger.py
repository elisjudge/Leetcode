class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        reverse_s = s[::-1]
        total = 0
        
        for letter in reverse_s:
            total += values[letter]

            if letter == "I" and total >= 5:
                total -= 2
            elif letter == "X" and total >= 50:
                total -= 20
            elif letter == "C" and total >= 500:
                total -= 200

        return total    


s = Solution()

s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

print(s.romanToInt(s3))
