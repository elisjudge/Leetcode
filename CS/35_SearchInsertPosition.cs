namespace LeetCodeSolutions {
    public static class SearchInsertPosition {
        public static int Solution (int[] nums, int target) {
            int m;
            int l = 0;
            int r = nums.Length - 1;

            while (l <= r) {
                m = (l + r) / 2;
                if (nums[m] > target) {
                    r = m - 1;
                } else if (nums[m] < target) {
                    l = m + 1;
                } else {
                    return m;
                }
            }
            return l;
        }
        public static void RunTests() {
            Console.WriteLine("Running Length Of Search Insert Tests...");

            var testCases = new List<(int[], int, int)> {
                (new int[] {1, 3, 5, 6}, 5, 2),
                (new int[] {1, 3, 5, 6}, 2, 1),
                (new int[] {1, 3, 5, 6}, 7, 4),
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
