namespace LeetCodeSolutions {
    public static class PlusOne {
        public static int[] Solution(int[] digits) {
        for (int i = digits.Length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits; 
            }
            digits[i] = 0;
        }

        int[] one = new int[] { 1 };
        int[] result = one.Concat(digits).ToArray();
        return result;
        }

        public static void RunTests() {
            Console.WriteLine("Running Length Of Plus One Tests...");

            var testCases = new List<(int[], int[])> {
                (new int[] {1, 2, 3}, new int[] {1, 2, 4}),
                (new int[] {1, 2, 3, 4}, new int[] {1, 2, 3, 5}),
                (new int[] {9, 9, 9}, new int[] {1, 0, 0, 0}),
                (new int[] {4, 3, 2, 1}, new int[] {4, 3, 2, 2}),
                (new int[] {9}, new int[] {1, 0}),
            };

            foreach (var (digits, expected) in testCases) {
                try {
                    var result = Solution(digits);
                    Console.WriteLine(
                        $"Input: {string.Join(",", digits)} " +
                        $"Expected: {string.Join(",", expected)} Result: {string.Join(",", result)}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}
