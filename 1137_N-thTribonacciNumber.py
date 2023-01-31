class Solution:
    def __init__(self) -> None:
        pass

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        F = [0]*(n+1)
        F[1], F[2] = 1, 1 

        j = 4-1
        while j < len(F):
            F[j] = F[j-1] + F[j-2] + F[j-3]
            j+=1
        return F[n]


s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(25))

