class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mn = m + n
        merged_array = []
        median_position = mn // 2 + 1
        ptr1, ptr2 = 0, 0
        count = 0

        while ptr1 < m and ptr2 < n:
            if count == median_position:
                break
            if nums1[ptr1] <= nums2[ptr2]:
                merged_array.append(nums1[ptr1])
                ptr1 += 1
            elif nums2[ptr2] < nums1[ptr1]:
                merged_array.append(nums2[ptr2])
                ptr2 += 1
            count += 1
            
        if ptr2 == n and count < median_position:
            while ptr1 < m:
                if count == median_position:
                    break
                merged_array.append(nums1[ptr1])
                ptr1 += 1
                count += 1

        elif ptr1 == m and count < median_position:
            while ptr2 < n:
                if count == median_position:
                    break
                merged_array.append(nums2[ptr2])
                ptr2 += 1
                count += 1
        
        if mn % 2 != 0 or mn == 1:
            return merged_array.pop()
        else:
            val1 = merged_array.pop() 
            val2 = merged_array.pop()
            return (val1 + val2) / 2


s = Solution()

print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(s.findMedianSortedArrays(nums1 = [], nums2 = [1]))
print(s.findMedianSortedArrays(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]))
print(s.findMedianSortedArrays(nums1 = [2,2,4,4], nums2 = [2,2,2,4,4]))
print(s.findMedianSortedArrays(nums1 = [2,3,4,5], nums2 = []))



