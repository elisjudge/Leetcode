class Solution:
    def __init__(self) -> None:
        pass

    def maxProfit(self, prices: list[int]) -> int:
        
        l, r = 0, 1 
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1
        
        return maxP


prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [2,7,6,4,3,1,7]
prices4 = [2,7,6,4,3,1,5]

s = Solution()
print(s.maxProfit(prices1))
print(s.maxProfit(prices2))
print(s.maxProfit(prices3))
print(s.maxProfit(prices4))