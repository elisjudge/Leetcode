class Solution:
    def intToRoman(self, num: int) -> str:
        letterValues = [("M", 1000), ("CM", 900), ("D", 500), 
                        ("CD", 400), ("C", 100), ("XC", 90),
                        ("L", 50), ("XL", 40), ("X", 10),
                        ("IX", 9), ("V", 5), ("IV", 4), 
                        ("I", 1)]
        roman = ""

        for letter, value in letterValues:
            while (num / value) >= 1:
                roman += letter
                num -= value
        return roman
    

s = Solution()
num = 1469

print(s.intToRoman(num))
            