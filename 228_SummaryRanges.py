class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)
        range_section = False
        range_list = []
        
        for i in range(n):
            if not range_section:
                range_start = nums[i]
                range_section = True

            if i+1 == n:
                if range_start == nums[i]:
                    range_string = f"{range_start}"
                    range_list.append(range_string)
                elif range_start != nums[i]:
                    range_end = f"{nums[i]}"
                    range_string = f"{range_start}->{range_end}"
                    range_list.append(range_string)

            elif nums[i+1] - nums[i] != 1:
                if range_start == nums[i]:
                    range_string = f"{range_start}"
                    range_list.append(range_string)

                elif range_start != nums[i]:                    
                    range_end = f"{nums[i]}"
                    range_string = f"{range_start}->{range_end}"
                    range_list.append(range_string)

                range_section= False    

        return range_list
                

s=Solution()
nums1 = [0,1,2,4,5,7]
nums2 = [0,2,3,4,6,8,9]
print(s.summaryRanges(nums2))


