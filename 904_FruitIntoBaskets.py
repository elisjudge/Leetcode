class Solution:
    def __init__(self) -> None:
        pass

    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) in range(0, 3):
            return len(fruits)
       
        l, r = 0, 0
        fruit_count = {}
        max_fruit = 0
        
        while r < len(fruits):
            if fruits[r] in fruit_count:
                fruit_count[fruits[r]] += 1
            else:
                fruit_count[fruits[r]] = 1
            
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l += 1
            
            max_fruit = max(max_fruit, r - l + 1)
            r += 1
            
        return max_fruit

fruits1 = [1,2,1] # 3
fruits2 = [0,1,2,2] # 3
fruits3 = [1,2,3,2,2] # 4
fruits4 = [3,3,3,1,2,1,1,2,3,3,4] #5
        #  0 1 2 3 4 5 6 7 8 9 10
fruits5 = [0,0,0,0,0,0,0,0,0,0,0] #11
        #  0 1 2 3 4 5 6 7 8 9 10
fruits6 = [0,1,6,6,4,4,6]
        #  0 1 2 3 4 5 6        
        
            
s=Solution()

print(s.totalFruit(fruits1))
print(s.totalFruit(fruits2))
print(s.totalFruit(fruits3))
print(s.totalFruit(fruits4))
print(s.totalFruit(fruits5))
print(s.totalFruit(fruits6))






    




