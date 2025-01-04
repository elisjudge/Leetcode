class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        hashmap = {}

        if len(s_list) != len(pattern):
            return False
        
        if len(set(s_list)) != len(set(pattern)):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = s_list[i]
            else:
                if hashmap[pattern[i]] != s_list[i]:
                    return False
        return True


s = Solution()
pattern1, s1 = "abba", "dog cat cat dog"
pattern2, s2 = "abba", "dog cat cat fish"
pattern3, s3 = "aaaa", "dog cat cat dog"
pattern4, s4 = "abba", "dog dog dog dog"
pattern5, s5 = "abbca", "dog cat dog fish dog"

print(s.wordPattern(pattern5, s5))