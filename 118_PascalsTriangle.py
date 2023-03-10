class Solution:

    def __init__(self) -> None:
        pass

    def generatePascal(self, numRows: int) -> list[list[int]]:

        # Set base result
        result = [[1]]

        # Because the result already contains the answer to nRows = 1, 
        # we don't want to do anything elseif nRows = 1.
        # So subtracting 1 from nRows = 1 will mean that just the 
        # result is returned as for i in range(0) will do nothing. 

        for i in range(numRows - 1):
            # Lets add 0 to the start and end of the last array in the list of arrays. 
            temp = [0] + result[-1] + [0]

            # Generate the subsequent row of the triangle.
            triangleRow = []
            
            # The length of each subsequent row must increase by 1.
            # So for the length of the most recent array in the list plus 1,
            # we will iterate over the temp list, compute j + (j+1), and add it to
            # as a value in the next row.
            # This will perfectly iterate over the list each time as 
            # len(temp) = ( len(result[-1] + 1) ) + 1

            for j in range(len(result[-1]) + 1):
                triangleRow.append(temp[j]+ temp[j+1])
            result.append(triangleRow)
        return result


s = Solution()


print(s.generatePascal(100))


