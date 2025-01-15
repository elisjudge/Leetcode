class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = len(str1), len(str2)

        def isDivisor(length):
            if len_str1 % length or len_str2 % length:
                return False

            factor1, factor2 = len_str1 // length, len_str2 // length
            if str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2:
                return True

            return False

        for str_length in range(min(len_str1, len_str2), 0, -1):
            if isDivisor(str_length):
                return str1[:str_length]
        return ""

s = Solution()

s1A, s1B = "ABCABC", "ABC"
s2A, s2B = "ABABAB", "ABAB"
s3A, s3B = "LEET", "CODE"

print(s.gcdOfStrings(s1A, s1B))
print(s.gcdOfStrings(s2A, s2B))
print(s.gcdOfStrings(s3A, s3B))