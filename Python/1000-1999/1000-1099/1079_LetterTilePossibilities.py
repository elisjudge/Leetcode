class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_counts = {tile:0 for tile in set(tiles)}
        for tile in tiles:
            tile_counts[tile] += 1 
        visited = set()
        possibilities = 0
        
        def backtracking():
            nonlocal possibilities
            possibilities += 1

            for tile in tile_counts:
                if tile_counts[tile] > 0:
                    tile_counts[tile] -= 1
                    backtracking()
                    tile_counts[tile] += 1
                
        for tile in tiles:
            if tile in visited:
                continue
            else:
                visited.add(tile)
                tile_counts[tile] -= 1
                backtracking()
                tile_counts[tile] += 1

        return possibilities


s = Solution()

testcases = [
    {"tiles": "AAB", "expected": 8},
    {"tiles": "AAABBC", "expected": 188},
    {"tiles": "V", "expected": 1},
]

for i, testcase in enumerate(testcases):
    output = s.numTilePossibilities(testcase["tiles"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")