/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = new Array(arr.length).fill(0);
    for (let i = 0; i < arr.length; i++) {
        result[i] = fn(arr[i], i);
    }
    return result;
};

const testCases = [
    {arr: [1,2,3], fn: function plusone(n) { return n + 1; }, expected: [2,3,4] },
    {arr: [1,2,3], fn: function plusI(n, i) { return n + i; }, expected: [1,3,5] },
    {arr: [10,20,30], fn: function constant() { return 42; }, expected: [42,42,42] },
]

testCases.forEach((testCase, i) => {
    const output = map(testCase.arr, testCase.fn);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});