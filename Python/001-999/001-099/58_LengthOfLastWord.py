class Solution1:
    def __init__(self) -> None:
        pass

    def lengthOfLastWord(self, s: str) -> int:
        """
        Easy cheating solution using str.split()
        """
        strList = s.split()
        return len(strList[-1])

class Solution2:
    def __init__(self) -> None:
        pass

    def lengthOfLastWord(self, s: str) -> int:
        """
        This solution will start from the end of the string 
        and begin counting the number of characters in a word.
        Any whitespaces will be ignored before beginning the count.
        As soon as a subsequent whitespace is hit, or the end of the string
        is reached, then the length of the word will be returned.
        Length of word will be done by counting characters.
        Time complexirty = o(n), memory complexity = o(1)
        """

        i, length = len(s)-1, 0

        while s[i] == " ":
            i-= 1
        
        while i >= 0 and s[i] != " ":
            length +=1
            i-=1
        return length
        
        

s1 = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"

sol1 = Solution1()
sol2 = Solution2()


print("Solution 1")
print(sol1.lengthOfLastWord(s1))
print(sol1.lengthOfLastWord(s2))
print(sol1.lengthOfLastWord(s3))
print()
print("Solution 2")
print(sol2.lengthOfLastWord(s1))
print(sol2.lengthOfLastWord(s2))
print(sol2.lengthOfLastWord(s3))
