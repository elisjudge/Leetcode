class Solution:
    def __init__(self) -> None:
        pass
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        prev, l, r = 0, 0, 1

        if len(flowerbed)== 1:
            if n == 0:
                return True
            elif n == 1 and flowerbed[l] == 0:
                return True
            else:
                return False


        while r < len(flowerbed):
            if n == 0:
                return True
            
            if prev == 0 and flowerbed[l] == 0 and flowerbed[r] == 0:
                flowerbed[l] = 1
                n -= 1
            
            prev = flowerbed[l]
            l+=1
            r+=1
        
        if prev == 0 and flowerbed[l] == 0:
            flowerbed[l] = 1
            n-= 1
        
        return n == 0
     

flowerbed1, n1 = [1,0,0,0,1], 1 # True
flowerbed2, n2 = [1,0,0,0,1], 2 # False
flowerbed3, n3 = [0], 0 # True
flowerbed4, n4 = [1], 0 # True
flowerbed5, n5 = [0], 1 # True
flowerbed6, n6 = [1], 1 # False

s = Solution()
print(s.canPlaceFlowers(flowerbed1, n1))
print(s.canPlaceFlowers(flowerbed2, n2))
print(s.canPlaceFlowers(flowerbed3, n3))
print(s.canPlaceFlowers(flowerbed4, n4))
print(s.canPlaceFlowers(flowerbed5, n5))
print(s.canPlaceFlowers(flowerbed6, n6))



