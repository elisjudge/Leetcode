/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => fn(a) - fn(b));
};

const testCases = [
    { arr: [5, 4, 1, 2, 3], fn: (x) => x, expected: [1, 2, 3, 4, 5] },
    { arr: [{ x: 1 }, { x: 0 }, { x: -1 }], fn: (d) => d.x, expected: [{ x: -1 }, { x: 0 }, { x: 1 }] },
    { arr: [[3, 4], [5, 2], [10, 1]], fn: (x) => x[1], expected: [[10, 1], [5, 2], [3, 4]] }
];

testCases.forEach(({ arr, fn, expected }, i) => {
    const result = sortBy(arr, fn);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
