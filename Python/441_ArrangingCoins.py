class Solution:
    def __init__(self) -> None:
        pass
    def arrangeCoins(self, n: int) -> int:
        """
        Will solve this using a binary search algorithm
        """

        l, r = 1, n
        max_rows = 0

        while l <=r:
            # Mid point will be candidate for max rows
            m = (l+r) // 2
            coins = (m/2) * (m+1) #Gauss formula
            if coins > n:
                r = m - 1
            else:
                l = m + 1
                max_rows = max(m, max_rows)
        return max_rows


s= Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))

print(s.arrangeCoins(101))


