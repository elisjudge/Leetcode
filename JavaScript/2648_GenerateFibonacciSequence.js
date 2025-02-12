/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

/**
 * Example Test Cases for fibGenerator
 */

// Create a new generator instance
const gen = fibGenerator();

// Define the test cases
const testCases = [
    {
        callCount: 0,
        expected: []
    },
    {
        callCount: 1,
        expected: [0]
    },
    {
        callCount: 2,
        expected: [0, 1]
    },
    {
        callCount: 5,
        expected: [0, 1, 1, 2, 3]
    },
    {
        callCount: 10,
        expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    }
];

// Run the test cases
testCases.forEach(({ callCount, expected }, i) => {
    const gen = fibGenerator(); // New generator for each test case
    const result = [];

    for (let j = 0; j < callCount; j++) {
        result.push(gen.next().value);
    }

    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
