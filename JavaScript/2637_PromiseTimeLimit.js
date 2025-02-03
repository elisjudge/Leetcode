/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            const fnPromise = fn(...args);

            const timeoutPromise = new Promise((_, rejectTimeout) => {
                setTimeout(() => rejectTimeout("Time Limit Exceeded"), t);
            });

            Promise.race([fnPromise, timeoutPromise])
                .then(resolve)
                .catch(reject);
        });
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */


const testCases = [
    {
        fn: async (n) => {
            await new Promise(res => setTimeout(res, 100));
            return n * n;
        },
        inputs: [5],
        t: 50,
        expected: { rejected: "Time Limit Exceeded" }
    },
    {
        fn: async (n) => {
            await new Promise(res => setTimeout(res, 100));
            return n * n;
        },
        inputs: [5],
        t: 150,
        expected: { resolved: 25 }
    },
    {
        fn: async (a, b) => {
            await new Promise(res => setTimeout(res, 120));
            return a + b;
        },
        inputs: [5, 10],
        t: 150,
        expected: { resolved: 15 }
    },
    {
        fn: async () => {
            throw "Error";
        },
        inputs: [],
        t: 1000,
        expected: { rejected: "Error" }
    }
];

testCases.forEach(async ({ fn, inputs, t, expected }, i) => {
    const limited = timeLimit(fn, t);
    const start = performance.now();
    let result;

    try {
        const res = await limited(...inputs);
        result = { resolved: res, time: Math.floor(performance.now() - start) };
    } catch (err) {
        result = { rejected: err, time: Math.floor(performance.now() - start) };
    }

    const success =
        expected.resolved !== undefined
            ? result.resolved === expected.resolved
            : result.rejected === expected.rejected;

    console.log(`Test Case ${i + 1}:`, success ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
