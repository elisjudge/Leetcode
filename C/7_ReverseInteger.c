#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int reverse(int x) {
    int revNum = 0;

    while (x != 0) {
        int lastDigit = x % 10;

        if (revNum > INT_MAX / 10 || (revNum == INT_MAX / 10 && lastDigit > 7)) {
            return 0; 
        }
        if (revNum < INT_MIN / 10 || (revNum == INT_MIN / 10 && lastDigit < -8)) {
            return 0; 
        }

        revNum = revNum * 10 + lastDigit;
        x /= 10;
    }

    return revNum;
}

void runTests() {
    printf("Running Reverse Integer Tests...\n");

    struct TestCase {
        int input;
        int expected;
    } testCases[] = {
        {-1234, -4321},
        {1534236469, 0},
        {123, 321},
        {120, 21}
    };

    int numTests = sizeof(testCases) / sizeof(testCases[0]);

    for (int i = 0; i < numTests; i++) {
        int result = reverse(testCases[i].input);
        if (result == testCases[i].expected) {
            printf("Test Case %d Passed: Input: %d, Expected: %d, Result: %d\n",
                i + 1, testCases[i].input, testCases[i].expected, result);
        } else {
            printf("Test Case %d Failed: Input: %d, Expected: %d. Result: %d\n",
                i + 1, testCases[i].input, testCases[i].expected, result);
        }
    }
}

int main() {
    runTests();
    return 0;
}