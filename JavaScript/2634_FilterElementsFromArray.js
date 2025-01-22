/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = new Array();
    for (let i = 0; i < arr.length; i++) {
        const output = fn(arr[i], i);
        if (Boolean(output)) {
            result.push(arr[i]);
        }
    }
    return result;
};

const testCases = [
    {arr: [0,10,20,30], fn: function greaterThan10(n) { return n > 10; }, expected: [20,30] },
    {arr: [1,2,3], fn: function firstIndex(n, i) { return i === 0; }, expected: [1] },
    {arr: [-2,-1,0,1,2], fn: function plusOne(n) { return n + 1 }, expected: [-2,0,1,2] },
]

testCases.forEach((testCase, i) => {
    const output = filter(testCase.arr, testCase.fn);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});