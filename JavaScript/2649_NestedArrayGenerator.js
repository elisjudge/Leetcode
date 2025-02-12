/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    for (const element of arr) {
        if (Array.isArray(element)) {
            yield* inorderTraversal(element);
        } else {
            yield element;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */

/**
 * Example Test Cases for inorderTraversal
 */

// Define the test cases
const testCases = [
    {
        input: [[[6]], [1, 3], []],
        expected: [6, 1, 3]
    },
    {
        input: [],
        expected: []
    },
    {
        input: [1, [2, [3, [4, 5]]]],
        expected: [1, 2, 3, 4, 5]
    },
    {
        input: [[[[[7]]]]],
        expected: [7]
    },
    {
        input: [10, [20, [30, [40, 50]]], 60],
        expected: [10, 20, 30, 40, 50, 60]
    },
    {
        input: [[1, 2, 3], [[4, 5], [6]], 7, [[8]]],
        expected: [1, 2, 3, 4, 5, 6, 7, 8]
    },
    {
        input: [[[[[[9]]]]]], // Deep nesting
        expected: [9]
    },
    {
        input: [[], [[]], [[[]]], 42, [[[]], [43]]],
        expected: [42, 43]
    }
];

// Run the test cases
testCases.forEach(({ input, expected }, i) => {
    const gen = inorderTraversal(input); // Create new generator for each test case
    const result = [];

    for (const value of gen) {
        result.push(value);
    }

    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
