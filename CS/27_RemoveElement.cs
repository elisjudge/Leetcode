namespace LeetCodeSolutions {
    public static class RemoveElement {
        public static int Solution(int[] nums, int val) {
            int k = 0;

            for (int i = 0; i < nums.Length; i++) {
                if (nums[i] != val) {
                    nums[k] = nums[i];
                    k++;
                }
            }
            return k;
        }
        public static void RunTests() {
            Console.WriteLine("Running Length Of Remove Element Tests...");

            var testCases = new List<(int[], int, int)> {
                (new int[] {3, 2, 2, 3}, 3, 2),
                (new int[] {0, 1, 2, 2, 3, 0, 4, 2}, 2, 5),
            };

            foreach (var (nums, val, expected) in testCases) {
                try {
                    var result = Solution(nums, val);
                    Console.WriteLine(
                        $"Input: {string.Join(",", nums)} Val: {val} " +
                        $"Expected: {expected} Result: {result}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}