namespace LeetCodeSolutions {
    public static class CanPlaceFlowers {
        public static bool Solution(int[] flowerbed, int n) {
            // Create new array in [0, ...flowerbed, 0]
            int[] f = new int[flowerbed.Length + 2];
            f[0] = 0;
            Array.Copy(flowerbed, 0, f, 1, flowerbed.Length);
            f[f.Length - 1] = 0;

            for (int i = 1; i < f.Length - 1; i++) {
                if (f[i - 1] == 0 && f[i] == 0 && f[i + 1] == 0) {
                    f[i] = 1;
                    n --;
                }
            }
            return n <= 0;
        }
        public static void RunTests() {
            Console.WriteLine("Running Can Place Flowers Tests...");

            var testCases = new List<(int[], int, bool)> {
                (new int[] { 1, 0, 0, 0, 1 }, 1, true),
                (new int[] { 1, 0, 0, 0, 1 }, 2, false),
                (new int[] { 0, 0, 0 }, 2, true),
                (new int[] { 0, 0, 0 }, 3, false),
                (new int[] { 0, 0, 1 }, 1, true),
                (new int[] { 1, 0, 0 }, 1, true),
                (new int[] { 0, 0, 1 }, 2, false),
                (new int[] { 0, 1 }, 1, false),
                (new int[] { 0, 0 }, 2, false),
                (new int[] { 0, 0 }, 1, true)
            };

            foreach (var (flowerbed, n, expected) in testCases) {
                try {
                    var result = Solution(flowerbed, n);
                    Console.WriteLine(
                        $"Input: {string.Join(",", flowerbed)} n Flowers: {n} " +
                        $"Expected: {string.Join(",", expected)} Result: {string.Join(",", result)}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}