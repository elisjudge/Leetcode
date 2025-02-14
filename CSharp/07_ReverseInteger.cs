namespace LeetCodeSolutions {
    public static class ReverseInteger {
        public static int Solution(int x) {
            bool negative = x < 0;
            int revNum = 0;

            if (negative) {
                x = -x;
            }

            while (x > 0) {
                int lastDigit = x % 10;

                if (revNum > (int.MaxValue - lastDigit) / 10) {
                    return 0;
                }

                revNum = revNum * 10 + lastDigit;
                x /= 10;
            }

            return negative ? -revNum : revNum;
        }
    

        public static void RunTests() {
            Console.WriteLine("Running Reverse Integer Tests...");
            
            var testCases = new List<(int, int)> {
                (-1234, -4321),
                (1534236469, 0),
                (123, 321),
                (120, 21)
            };

            foreach (var (x, expected) in testCases) {
                try {
                    var result = Solution(x);
                    Console.WriteLine(
                        $"Input: {x}, Expected: {expected}, Result: {result}" 
                    );
                } catch (Exception ex) {
                    Console.WriteLine($"Test Failed: {ex.Message}");
                }
            }
        }
    }
}