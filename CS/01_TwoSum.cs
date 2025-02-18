namespace LeetCodeSolutions {
    public static class TwoSum {
        public static int[] Solution(int[] nums, int target) {
            Dictionary<int, int> hash_map = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++) {
                int diff = target - nums[i];
                if (hash_map.ContainsKey(diff)) {
                    return new int[] { hash_map[diff], i };
                }
                hash_map[nums[i]] = i;
            }
            throw new Exception("No solution found");
        }

        public static void RunTests() {
            Console.WriteLine("Running Two Sum Tests...");

            var testCases = new List<(int[], int, int[])> {
                (new int[] { 2, 7, 11, 15 }, 9, new int[] { 0, 1 }),
                (new int[] { 3, 2, 4 }, 6, new int[] { 1, 2 }),
                (new int[] { 3, 3 }, 6, new int[] { 0, 1 })
            };

            foreach (var (nums, target, expected) in testCases) {
                try {
                    var result = Solution(nums, target);
                    Console.WriteLine(
                        $"Input: {string.Join(",", nums)} Target: {target} " +
                        $"Expected: {string.Join(",", expected)} Result: {string.Join(",", result)}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}
