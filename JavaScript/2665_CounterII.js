/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;

    return {
        increment: () => {
            return ++count;
        },
        decrement: () => {
            return --count;
        },
        reset: () => {
            count = init;
            return count;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

const testCases = [
    {
        init: 5,
        calls: ["increment", "reset", "decrement"],
        expected: [6,5,4]
    },
    {
        init: 0,
        calls: ["increment","increment","decrement","reset","reset"],
        expected: [1,2,1,0,0]
    },
];

testCases.forEach((testCase, i) => {
    const counter = createCounter(testCase.init);
    const output = testCase.calls.map(call => counter[call]());
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});