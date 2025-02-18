namespace LeetCodeSolutions {
    public static class MergeSortedArray {
        public static void Solution(int[] nums1, int m, int[] nums2, int n) {
            int end = m + n - 1;
            while (m > 0 && n > 0) {
                if (nums1[m - 1] >= nums2[n - 1]) {
                    nums1[end] = nums1[m - 1];
                    m--;
                } else {
                    nums1[end] = nums2[n - 1];
                    n--;
                }
                end--;
            }
            while (n > 0) {
                nums1[end] = nums2[n - 1];
                n--;
                end--;
            }
        }
        public static void RunTests() {
            Console.WriteLine("Running Length Of Merge Tests...");

            var testCases = new List<(int[], int, int[], int, int[])> {
                (
                    new int[] {1, 2, 3, 0, 0, 0}, 
                    3, 
                    new int[] {2, 5, 6},
                    3,
                    new int[] {1, 2, 2, 3, 5, 6}
                ),
                (
                    new int[] {1},
                    1,
                    new int[] {},
                    0,
                    new int[] {1}
                ),
                (
                    new int[] {0}, 
                    0, 
                    new int[] {1}, 
                    1,
                    new int[] {1}
                ),
            };

            foreach (var (nums1, m, nums2, n, expected) in testCases) {
                try {
                    int[] result = nums1;
                    
                    Solution(result, m, nums2, n);
                    Console.WriteLine(
                        $"Input: {string.Join(",", nums1)}, Merged List: {string.Join(",", nums2)} Vals: m {m},  n {n} " +
                        $"Expected: {string.Join(",", expected)} Result: {string.Join(",", result)}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}