class Solution:

    def __init__(self) -> None:
        pass
    
    # def replaceElements(self, arr: list[int]) -> list[int]:
    #     """ Unoptimal solution, runs on o(n^2) """
    #     result = []
        
    #     for i in range(len(arr)):
    #         if len(arr[i+1:]) >= 1:
    #             result.append(sorted(arr[i+1:])[-1])
    #         else: 
    #             result.append(-1)
    #     return result

    def replaceElements(self, arr: list[int]) -> list[int]:
        """Will iterate over the array in reverse and will take the 
        greater of two values at each position and set it as the subsequent 
        value."""
        
        # initial max = -1 because this must be the end of the array according to 
        # instructions.

        # Iterate in reverse
        
        # new max = max(oldmax, arr[i])

        rightMax = -1

        for i in range(len(arr)-1,-1,-1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr



s = Solution()

arr1 = [17,18,5,4,6,1]
arr2 = [400]
print(s.replaceElements(arr1))

