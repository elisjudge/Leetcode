namespace LeetCodeSolutions {
    public static class RomanToInteger {
       public static int Solution(string s) {
           Dictionary<char, int> letterValues = new Dictionary<char, int> {
               {'I', 1},
               {'V', 5},
               {'X', 10},
               {'L', 50},
               {'C', 100},
               {'D', 500},
               {'M', 1000}
           };

           char[] stringArray = s.ToCharArray();
           Array.Reverse(stringArray);
           string sReversed = new string(stringArray); 
           int total = 0;

           for (int i = 0; i < sReversed.Length; i++) {
               total += letterValues[sReversed[i]];
               if (sReversed[i] == 'I' && total >= 5) {
                   total -= 2;
               } else if (sReversed[i] == 'X' && total >= 50) {
                   total -= 20; 
               } else if (sReversed[i] == 'C' && total >= 500) {
                   total -= 200; 
               }
           }
           return total; 
       }

       public static void RunTests() {
            Console.WriteLine("Running Roman To Integer Tests...");

            var testCases = new List<(string, int)> {
                ("III", 3),
                ("LVIII", 58),
                ("MMMDCCXLIX", 3749),
                ("MCDLXIX", 1469),
                ("MCMXCIV", 1994)
            };

            foreach (var (s, expected) in testCases) {
                try {
                    var result = Solution(s);
                    if (result == expected) {
                        Console.WriteLine(
                            $"Test Passed: Input: {s}, Expected: {expected}, Result: {result}"
                        );
                    } else {
                        Console.WriteLine(
                            $"Test Falied: Input: {s}, Expected: {expected}, Result: {result}"
                        );
                    }
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
       } 
    }
}