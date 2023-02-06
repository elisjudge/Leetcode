class Solution:
    
    def __init__(self) -> None:
        pass
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[end] = nums1[m-1]
                m -= 1
            else:
                nums1[end] = nums2[n-1]
                n -= 1
            end -= 1
        
        while n > 0:
            nums1[end] = nums2[n-1]
            n -= 1
            end -= 1

        print(nums1)


numsA1, m1, numsB1, n1 = [1,2,3,0,0,0], 3, [2,5,6],  3
numsA2, m2, numsB2, n2 = [1], 1, [], 0
numsA3, m3, numsB3, n3 = [0], 0, [1], 1            

s = Solution()

s.merge(numsA1, m1, numsB1, n1)
s.merge(numsA2, m2, numsB2, n2)
s.merge(numsA3, m3, numsB3, n3)
