/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init;
    
    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]);
    }
    return result;    
};

const testCases = [
    {nums: [1,2,3,4], fn: function sum(accum, curr) { return accum + curr; }, init: 0,  expected: 10 },
    {nums: [1,2,3,4], fn: function sum(accum, curr) { return accum + curr * curr; }, init: 100, expected: 130 },
    {nums: [], fn: function sum(accum, curr) { return 0; }, init: 25, expected: 25 },
]

testCases.forEach((testCase, i) => {
    const output = reduce(testCase.nums, testCase.fn, testCase.init);
    if (output === testCase.expected) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});