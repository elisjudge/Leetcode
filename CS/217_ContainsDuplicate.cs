namespace LeetCodeSolutions {
    public static class ContainsDuplicate {
        public static bool Solution(int[] nums) {
            HashSet<int> hashSet = new HashSet<int>();

            foreach (int num in nums) {
                if (hashSet.Contains(num)) {
                    return true;
                }
                hashSet.Add(num);
            }
            return false;
        }

        public static void RunTests() {
            Console.WriteLine("Running Contains Duplicate");

            var testCases = new List<(int[] nums, bool expected)> {
                (new int[] {1, 2, 3, 1}, true),
                (new int[] {1, 2, 3, 4}, false),
                (new int[] {1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true)
            };

            foreach (var (nums, expected) in testCases) {
                try {
                    var result = Solution(nums);
                    Console.WriteLine(
                        $"Test Passed: Input: [{string.Join(", ", nums)}], Expected {expected}, Result: {result}" 
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}

