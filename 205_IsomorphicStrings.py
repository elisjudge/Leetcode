class Solution:
    def __init__(self) -> None:
        pass
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}

        for i, j in zip(s,t):

            if i in hashmap and hashmap[i] == j:
                continue
            elif j in hashmap.values():
                return False
            elif i not in hashmap:
                hashmap[i] = j
            else:
                return False
        return True
            

s1, t1 = "egg", "add" # True
s2, t2 = "foo", "bar" #False
s3, t3 = "paper", "title" #True
s4, t4 = "badc", "baba" #false

s = Solution()

print(s.isIsomorphic(s1, t1))
print(s.isIsomorphic(s2, t2))
print(s.isIsomorphic(s3, t3))
print(s.isIsomorphic(s4, t4))