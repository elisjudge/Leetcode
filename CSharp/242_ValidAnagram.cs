namespace LeetCodeSolutions {
    public static class ValidAnagram {
        public static bool Solution(string s, string t) {
            if (s.Length != t.Length) {
                return false;
            }

            Dictionary<char, int> countS = new Dictionary<char, int>();
            Dictionary<char, int> countT = new Dictionary<char, int>();

            for (int i = 0; i < s.Length; i++) {
                countS[s[i]] = countS.ContainsKey(s[i]) ? countS[s[i]] + 1 : 1;
                countT[t[i]] = countT.ContainsKey(t[i]) ? countT[t[i]] + 1 : 1;
            }

            foreach (char c in countS.Keys) {
                if (countS[c] != (countT.ContainsKey(c) ? countT[c] : 0)) {
                    return false;
                }
            }

            return true;            
        }

        public static void RunTests() {
            Console.WriteLine("Running Valid Anagram");

            var testCases = new List<(string s, string t, bool expected)> {
                ("anagram",  "nagaram", true),
                ("rat",  "car", false)
            };

            foreach (var (s, t, expected) in testCases) {
                try {
                    var result = Solution(s, t);
                    if (result == expected) {
                        Console.WriteLine(
                            $"Test Passed: Input: {s}, {t}, Expected {expected}, Result: {result}" 
                        );
                    } else {
                        Console.WriteLine(
                            $"Test Failed: Input: {s}, {t}, Expected {expected}, Result: {result}" 
                        );
                    } 
                } catch (Exception ex) {
                    Console.WriteLine($"Test Error: {ex.Message}");
                }
            }
        }
    }
}