/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = {};
    
    return function(...args) {
        const key = JSON.stringify(args);
        if (key in cache) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    };
}


/** 
* let callCount = 0;
* const memoizedFn = memoize(function (a, b) {
*	 callCount += 1;
*   return a + b;
* })
* memoizedFn(2, 3) // 5
* memoizedFn(2, 3) // 5
* console.log(callCount) // 1 
*/

const testCases = [
    {
        fnName: "sum",
        fn: (a, b) => a + b,
        actions: ["call","call","getCallCount","call","getCallCount"],
        values: [[2,2],[2,2],[],[1,2],[]],
        expected: [4,4,1,3,2]
    },
    {
        fnName: "factorial",
        fn: function factorial(n) {
            return (n <= 1) ? 1 : (n * factorial(n - 1))
        },
        actions: ["call","call","call","getCallCount","call","getCallCount"],
        values: [[2],[3],[2],[],[3],[]],
        expected: [2,6,2,2,6,2]
    },
    {
        fnName: "fib",
        fn: function fib(n) {
            return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
        },
        actions: ["call","getCallCount"],
        values: [[5],[]],
        expected: [8,1]
    },
]

testCases.forEach((testCase, i) => {
    let callCount = 0;
    const memoizedFn = memoize(function (...args) {
        callCount++;
        return testCase.fn(...args);
    });
    
    const output = testCase.actions.map((action, index) => {
        if (action === "call") {
            return memoizedFn(...testCase.values[index]);
        } else if (action === "getCallCount") {
            return callCount;
        }
    });
    
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
}); 