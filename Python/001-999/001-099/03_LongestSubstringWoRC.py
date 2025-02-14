class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Brute Force Solution, o(n^2) time sliding window without hashing. Very Slow"""
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        result = 0 
        l, r  = 0, 1
        sub_string = s[l]

        while r < len(s):
            if s[r] not in sub_string:
                sub_string += s[r]
                r += 1
            else:
                l += 1 
                r = l + 1
                sub_string = s[l]

            result = max(result, (r - l))
        
        return result
    
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Sliding Window with Hash, o(n) time o(m) """
        result = 0 
        l = 0
        unique_chars = set()

        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            curr = len(unique_chars)
            
            result = max(result, curr)
        
        return result
    
s = Solution2()

print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("dvdf"))
