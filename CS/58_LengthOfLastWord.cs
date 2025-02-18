namespace LeetCodeSolutions {
    public static class LengthOfLastWord {
        public static int Solution(string s) {
            int i = s.Length - 1;
            int count = 0;
            while (s[i] == ' ') {
                i--;
            }
            while (i >= 0 && s[i] != ' ') {
                i--;
                count++;
            }
            return count;
        }
        public static void RunTests() {
            Console.WriteLine("Running Length Of Last Word Tests...");

            var testCases = new List<(string, int)> {
                ("Hello World", 5),
                ("   fly me   to   the moon  ", 4),
                ("luffy is still joyboy", 6),
            };

            foreach (var (s, expected) in testCases) {
                try {
                    var result = Solution(s);
                    Console.WriteLine(
                        $"Input: {s} " +
                        $"Expected: {expected} Result: {result}"
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}