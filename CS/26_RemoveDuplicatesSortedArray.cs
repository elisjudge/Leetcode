namespace LeetCodeSolutions {
    public static class RemoveDuplicates {
        public static int Solution(int[] nums) {
            int n = nums.Length;
            if (n == 1) return 1;

            int l = 0;
            int r = 1;
            int k = 1;

            while (r < n) {
                if (nums[l] == nums[r]) {
                    r++;
                } else {
                    nums[k] = nums[r];
                    k++;
                    l = r;
                    r++;
                }
            }
            return k;
        }
        public static void RunTests() {
            Console.WriteLine("Running Length Of Remove Duplicates Tests...");

            var testCases = new List<(int[], int)> {
                (new int[] {1, 1, 2}, 2),
                (new int[] {0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 5)
            };

            foreach (var (nums, expected) in testCases) {
                try {
                    var result = Solution(nums);
                    Console.WriteLine(
                        $"Input: {string.Join(",", nums)} " +
                        $"Expected: {expected} Result: {result}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}