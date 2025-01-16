class Solution:
    def computeHappy(self, n: int) -> int:
        return sum([int(digit)**2 for digit in str(n)])

    def isHappy(self, n: int) -> bool:
        """ This requires o(n) memory for hashset """
        hashset = set()
        
        while True:
            if n == 1:
                return True

            if n in hashset:
                return False
            else: 
                hashset.add(n)
                n = self.computeHappy(n)

    def isHappyOptimized(self, n: int) -> bool:
        """ o(1) memory solution using fast slow pointers """
        slow = n
        fast = n

        while True:
            slow = self.computeHappy(slow)
            fast = self.computeHappy(fast)
            fast = self.computeHappy(fast)
            
            if fast == 1:
                return True

            if slow == fast:
                return False


s = Solution()

print(s.isHappy(19))
print(s.isHappy(2))


print(s.isHappyOptimized(19))
print(s.isHappyOptimized(2))
print(s.isHappyOptimized(10))
