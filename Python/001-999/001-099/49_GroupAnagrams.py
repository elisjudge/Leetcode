from collections import defaultdict

class Solution:

    def __init__(self) -> None:
        pass

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """This function will create a dictionary that stores every
        combination of character counts for every string as the key,
        and the strings that consist of that given character count 
        as the values in a list.

        By character count, I mean counting the number of times a
        certain character appears in a string, not the length of the 
        string.        
        """

        # For this solution I will use defaultdict and pass it a list as the
        # default value. This is handy because I will be able to automatically
        # assign a value to keys that have not yet been added to the dictionary. 
        # Any default value is specified when the defaultdict is created, 
        # and it is returned whenever a nonexistent key is accessed.

        hashMap = defaultdict(list)

        for s in strs:
            # Create an array to count the 26 lowercase alphabet characters
            count = [0] * 26 # to map a ... z to.

            for char in s:
                # ensure that a is mapped to 0 and z is mapped to 25
                # using the Unicode value of the character
                count[ord(char) - ord("a")] += 1
            
            # Dictionaries cannot have lists as keys in python, so I will convert
            # to tuple to make the list immutable
            hashMap[tuple(count)].append(s)
        
        return hashMap.values()

sol = Solution()
strings = [["eat","tea","tan","ate","nat","bat"], 
           [""], 
           ["a"]]

for s in strings:
    print(sol.groupAnagrams(s))



