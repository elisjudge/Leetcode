class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)

        if n == 1:
            return 1
        
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)                   
        return sum(candies)

s = Solution()
ratings_1 = [1,0,2]    
ratings_2 = [1,2,2]
ratings_3 = [1,3,2,2,1]

print(s.candy(ratings_1))

