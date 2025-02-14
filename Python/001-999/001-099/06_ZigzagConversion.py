class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        hash_map = {}
        zig = True
        zag = False
        row = 0
        result = ""

        for i in range(numRows):
            hash_map[i] = []

        for char in s:
            if zig:
                hash_map[row].append(char)
                if row == numRows - 1:
                    zig = False
                    zag = True
                    row -= 1
                else:
                    row += 1

            elif zag:
                hash_map[row].append(char)
                if row == 0:
                    zig = True
                    zag = False
                    row += 1

                else:                    
                    row -= 1

        
        for i in range(numRows):
            for char in hash_map[i]:
                result += char
        
        return result
            

s = Solution()

print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))
print(s.convert("AB", 1))