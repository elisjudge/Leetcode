from collections import defaultdict

class Solution1:
    """
    I don't feel like this is the most optimal solution, or even a great solution, but it did well
    on runtime performance beating 92% of answers.

    But the runtime complexity is O(n^2) because I am iterating over the list twice, once to 
    build the dictionary, and then the second time to iterate over the dictionary to count the
    number of trusted people.
    
    """
    def __init__(self) -> None:
        pass

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        hashmap = defaultdict(list)

        for i in range(1, n+1):
            hashmap[i]


        for tru in trust:
            hashmap[tru[0]].append(tru[1])


        for item in hashmap.items():
            if len(item[1]) == 0:
                judge = item[0]
                count = 0
                for value in hashmap.values():
                    if judge in value:
                        count += 1
                
                if count == n-1:
                    return judge

        return -1

class Solution2:
    """
    An alternate solution that makes use of only lists, and doesn't use a dictionary.

    I don't think it is possible to derive the answer in O(n) time complexity for this problem
    as the entire list needs to be iterated over once to build the foundations to then
    search for an answer. For example, you might be able to spot a judge without iterating
    over the entire list, but you cannot begin to answer whether everyone trusts that judge 
    without first completing one run over the entire list.

    This code is shorter, but it appears to run slower.
    
    """
    def __init__(self) -> None:
        pass

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trustedBy = [0] * (n+1)
        trustingOf = [0] * (n+1)

        for a, b in trust:
            trustingOf[a] +=1
            trustedBy[b] +=1

        for i in range (1, n+1):
            if trustedBy[i] == n-1 and trustingOf[i] == 0:
                return i

        return -1
    
        
s1 = Solution1()
s2 = Solution2()


n1, trust1 = 2, [[1,2]]
n2, trust2 = 3, [[1,3],[2,3]]
n3, trust3 = 3, [[1,3],[2,3],[3,1]]
n4, trust4 = 3, [[1,3],[2,1]]
n5, trust5 = 4, [[1,3],[1,4],[2,3],[2,4],[4,3]] #3

   
print("Solution 1")
print(s1.findJudge(n1, trust1))
print(s1.findJudge(n2, trust2))
print(s1.findJudge(n3, trust3))
print(s1.findJudge(n4, trust4))
print(s1.findJudge(n5, trust5))
print()
print("Solution 2")
print(s2.findJudge(n1, trust1))
print(s2.findJudge(n2, trust2))
print(s2.findJudge(n3, trust3))
print(s2.findJudge(n4, trust4))
print(s2.findJudge(n5, trust5))
print()








