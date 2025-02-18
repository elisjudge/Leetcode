namespace LeetCodeSolutions {
    public static class IntegerToRoman {
        public static string Solution(int num) {
            Dictionary<string, int> letterValues = new Dictionary<string, int> {
                {"M", 1000},
                {"CM", 900},
                {"D", 500},
                {"CD", 400},
                {"C", 100},
                {"XC", 90},
                {"L", 50},
                {"XL", 40},
                {"X", 10},
                {"IX", 9},
                {"V", 5},
                {"IV", 4},
                {"I", 1}
            };
            string roman = "";

            foreach (var lV in letterValues) {
                while (num >= lV.Value) {
                    roman += lV.Key;
                    num -= lV.Value;
                }
            }
            return roman;
        }

        public static void RunTests() {
            Console.WriteLine("Running Integer To Roman Tests...");

            var testCases = new List<(int, string)> {
                (3749, "MMMDCCXLIX"),
                (1469, "MCDLXIX"),
                (58, "LVIII"),
                (1994, "MCMXCIV")
            };

            foreach (var (num, expected) in testCases) {
                try {
                    var result = Solution(num);
                    if (result == expected) {
                        Console.WriteLine(
                            $"Test Passed: Input: {num}, Expected: {expected}, Result: {result}"
                        );
                    } else {
                        Console.WriteLine(
                            $"Test Failed: Input: {num}, Expected: {expected}, Result: {result}"
                        );
                    } 
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }      
    }
}