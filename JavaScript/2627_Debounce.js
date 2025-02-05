/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer = null;
    
    return function(...args) {
        if (timer !== null) {
            clearTimeout(timer);
        }
        timer = setTimeout(() => {
            fn(...args);
            timer = null;
        }, t);
        
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

const testCases = [
    {
        t: 50,
        calls: [
            { t: 50, inputs: [1] },
            { t: 75, inputs: [2] }
        ],
        expected: [
            { t: 125, inputs: [2] }
        ]
    },
    {
        t: 20,
        calls: [
            { t: 50, inputs: [1] },
            { t: 100, inputs: [2] }
        ],
        expected: [
            { t: 70, inputs: [1] },
            { t: 120, inputs: [2] }
        ]
    },
    {
        t: 150,
        calls: [
            { t: 50, inputs: [1, 2] },
            { t: 300, inputs: [3, 4] },
            { t: 300, inputs: [5, 6] }
        ],
        expected: [
            { t: 200, inputs: [1, 2] },
            { t: 450, inputs: [5, 6] }
        ]
    }
];

// Function to run a single test case.
function runTestCase(testCase, caseIndex) {
    return new Promise((resolve) => {
        const { t, calls, expected } = testCase;
        const results = []; // to store { t, inputs } when the debounced function actually runs
        const startTime = Date.now();

        // Our test function: it records the relative time and the passed arguments.
        function testFn(...args) {
            results.push({
                t: Date.now() - startTime,
                inputs: args
            });
        }

        // Create the debounced version of testFn.
        const dTestFn = debounce(testFn, t);

        // Schedule each call according to the provided relative time.
        calls.forEach(call => {
            setTimeout(() => {
                dTestFn(...call.inputs);
            }, call.t);
        });

        // Determine how long we need to wait before checking the results.
        // We wait until after the last scheduled call plus the debounce delay, plus an extra margin.
        const maxCallTime = Math.max(...calls.map(call => call.t));
        const totalWaitTime = maxCallTime + t + 100;

        setTimeout(() => {
            // For timing comparisons, allow some tolerance (e.g., ±30ms)
            const timeTolerance = 30;
            let passed = true;

            if (results.length !== expected.length) {
                passed = false;
            } else {
                for (let i = 0; i < expected.length; i++) {
                    const expectedCall = expected[i];
                    const actualCall = results[i];
                    if (
                        Math.abs(actualCall.t - expectedCall.t) > timeTolerance ||
                        JSON.stringify(actualCall.inputs) !== JSON.stringify(expectedCall.inputs)
                    ) {
                        passed = false;
                        break;
                    }
                }
            }

            console.log(`Test Case ${caseIndex + 1}:`, passed ? "Passed ✅" : "Failed ❌");
            console.log("Expected:", expected);
            console.log("Actual:", results);
            console.log("--------------");
            resolve();
        }, totalWaitTime);
    });
}

// Run all test cases in sequence.
async function runAllTestCases() {
    for (let i = 0; i < testCases.length; i++) {
        await runTestCase(testCases[i], i);
    }
}

runAllTestCases();