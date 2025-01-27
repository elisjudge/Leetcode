/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let calls = 0
    
    return function(...args){
        if (!calls) {
            calls++;
            return fn(...args);
        }
        return undefined;
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */


const testCases = [
    {
        fn: (a, b, c) => a + b + c,
        calls: [
            { args: [1, 2, 3], expected: 6 },
            { args: [2, 3, 6], expected: undefined },
        ],
    },
    {
        fn: (a, b, c) => a * b * c,
        calls: [
            { args: [5, 7, 4], expected: 140 },
            { args: [2, 3, 6], expected: undefined },
            { args: [4, 6, 8], expected: undefined },
        ],
    },
];

testCases.forEach((testCase, i) => {
    const onceFn = once(testCase.fn);
    testCase.calls.forEach((call, j) => {
        const output = onceFn(...call.args);
        if (output === call.expected) {
            console.log(`Test Case ${i}-${j}: Passed. Expected: ${call.expected}, Output: ${output}`);
        } else {
            console.log(`Test Case ${i}-${j}: Failed. Expected: ${call.expected}, Output: ${output}`);
        }
    });
});