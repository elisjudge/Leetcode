class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        nrows, ncols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or 
                c < 0 or 
                r == nrows or 
                c == ncols or 
                (r,c) in visit or
                board[r][c] not in node.children):
                    return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(nrows):
            for c in range(ncols):
                dfs(r, c, root, "")
        
        return list(res)

s = Solution()

testcases = [
    {
        "board": [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]], 
        "words": ["oath","pea","eat","rain"], 
        "expected": ["eat","oath"]
    },
    {
        "board": [
            ["a","b"],
            ["c","d"]], 
        "words": ["abcb"], 
        "expected": []
    },
    {
        "board": [
            ["a","b","c","d"],
            ["s","a","a","t"],
            ["a","c","k","e"],
            ["a","c","d","n"]], 
        "words": ["bat","cat","back","backend","stack"], 
        "expected": ["cat","back","backend"]
    },
    {
        "board": [
            ["x","o"],
            ["x","o"]], 
        "words": ["xoxo"], 
        "expected": []
    }
]

for i, testcase in enumerate(testcases):
    output = s.findWords(testcase["board"], testcase["words"])

    if set(output) == set(testcase["expected"]):
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")