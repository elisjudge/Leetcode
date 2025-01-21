/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        return n++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

const testCases = [
    {
        n: 10,
        calls: ["call", "call", "call"],
        expected: [10,11,12]
    },
    {
        n: -2,
        calls: ["call","call","call","call","call"],
        expected: [-2,-1,0,1,2]
    },
]

testCases.forEach((testCase, i) => {
    const counter = createCounter(testCase.n);
    const output = testCase.calls.map(() => counter());
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});