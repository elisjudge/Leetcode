class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map, ransomNote_map = {}, {}

        for letter in magazine:
            if letter in magazine_map:
                magazine_map[letter] += 1
            elif letter not in magazine_map:
                magazine_map[letter] = 1

        for letter in ransomNote:
            if letter in ransomNote_map:
                ransomNote_map[letter] += 1
            elif letter not in ransomNote_map:
                ransomNote_map[letter] = 1

        for letter, n_letters in ransomNote_map.items():
            if letter not in magazine_map:
                return False
            if n_letters > magazine_map[letter]:
                return False
        
        return True


s = Solution()
ransomNote1, magazine1  = "a", "b"
ransomNote2, magazine2 = "aa", "ab"
ransomNote3, magazine3 = "aa", "aab"

print(s.canConstruct(ransomNote3, magazine3))

