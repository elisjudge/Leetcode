using System.Reflection;

namespace LeetCodeSolutions {
    class Program {
        static void Main(string[] args) {
            if (args.Length == 0) {
                Console.WriteLine("Please provide the name of the solution to run as a command-line argument.");
                Console.WriteLine("Example: dotnet run -- TwoSum");
                return;
            }

            string solutionName = args[0]; 
            Console.WriteLine($"Running Solution: {solutionName}");

            try {
                Type? solutionType = Type.GetType($"LeetCodeSolutions.{solutionName}")
                    ?? throw new Exception($"Solution '{solutionName}' not found.");
                
                MethodInfo? runTests = solutionType.GetMethod("RunTests")
                   ?? throw new Exception($"RunTests method not found in solution '{solutionName}'.");

                runTests.Invoke(null, null); 
            } catch (Exception ex) {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
