/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

const testCases = [
    {
        args: [],
        expected: "Hello World"
    },
    {
        args: [{},null,42],
        expected: "Hello World"
    },
]

testCases.forEach((testCase, i) => {
    const output = createHelloWorld(testCase.args);
    if (JSON.stringify(output()) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output())} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output())} `)
    } 
});