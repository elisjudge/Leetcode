/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        if (functions.length === 0) {
            return x;
        }
        for (let i = functions.length - 1; i >= 0; i--) {
            x = functions[i](x);
        }
        return x;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

const testCases = [
    {
        functions: [x => x + 1, x => x * x, x => 2 * x],
        x: 4,
        expected: 65
    },
    {
        functions: [x => 10 * x, x => 10 * x, x => 10 * x],
        x: 1,
        expected: 1000
    },
    {
        functions: [],
        x: 42,
        expected: 42
    },
]

testCases.forEach((testCase, i) => {
    const composeFn = compose(testCase.functions);
    const output = composeFn(testCase.x);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});