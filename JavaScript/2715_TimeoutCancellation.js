/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    const timer = setTimeout(() => {
        fn(...args);
    }, t);

    return () => {
        clearTimeout(timer);
    };
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */

const TIME_TOLERANCE_MS = 15;

const testCases = [
    {
        description: "Function executes because cancel is delayed beyond execution time",
        fn: (x) => x * 5,
        args: [2],
        t: 20,
        cancelTimeMs: 50,
        expected: [{ time: 20, returned: 10 }],
    },
    {
        description: "Function does not execute because cancel is called before execution time",
        fn: (x) => x ** 2,
        args: [2],
        t: 100,
        cancelTimeMs: 50,
        expected: [], // Cancelled before execution
    },
    {
        description: "Function executes because cancel is delayed beyond execution time",
        fn: (x1, x2) => x1 * x2,
        args: [2, 4],
        t: 30,
        cancelTimeMs: 100,
        expected: [{ time: 30, returned: 8 }],
    }
];

testCases.forEach(({ description, fn, args, t, cancelTimeMs, expected }, i) => {
    let result = [];
    
    const cancellableFn = cancellable((...args) => {
        const time = Date.now() - startTime;
        const returned = fn(...args);
        result.push({ time, returned });
    }, args, t);

    const startTime = Date.now();
    setTimeout(cancellableFn, cancelTimeMs);

    setTimeout(() => {
        console.log(`Test Case ${i + 1}: ${description}`);
        const passed = compareResults(result, expected);
        console.log(passed ? "Passed ✅" : "Failed ❌");
        console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
    }, Math.max(t, cancelTimeMs) + 10);
});

function compareResults(result, expected) {
    if (result.length !== expected.length) return false;

    return result.every((res, index) => {
        const exp = expected[index];
        const timeDifference = Math.abs(res.time - exp.time);
        return (
            timeDifference <= TIME_TOLERANCE_MS &&
            res.returned === exp.returned
        );
    });
}
