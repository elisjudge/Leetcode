/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) return arr;

    const result = [];

    for (const element of arr) {
        if (Array.isArray(element) && n > 0) {
            result.push(...flat(element, n - 1));
        } else {
            result.push(element);
        }
    }

    return result;
};

const testCases = [
    {
        arr: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
        depth: 0,
        expected: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
    },
    {
        arr: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
        depth: 1,
        expected: [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]
    },
    {
        arr: [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
        depth: 2,
        expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    },
    {
        arr: [],
        depth: 3,
        expected: []
    },
    {
        arr: [1, [2, [3, [4]]]],
        depth: 2,
        expected: [1, 2, 3, [4]]
    }
];

testCases.forEach(({ arr, depth, expected }, i) => {
    const result = flat(arr, depth);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
