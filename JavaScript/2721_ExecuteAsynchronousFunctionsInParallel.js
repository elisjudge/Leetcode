/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let remaining = functions.length;

        if (remaining === 0) {
            resolve(results);
            return;
        }

        functions.forEach((fn, index) => {
            fn()
                .then(result => {
                    results[index] = result;
                    remaining--;
                    if (remaining == 0) {
                        resolve(results);
                    }
                })
                .catch(error => {
                    reject(error);
                });
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */


const testCases = [
    {
        functions: [() => new Promise(res => setTimeout(() => res(5), 200))],
        expected: { resolved: [5] },
        shouldReject: false
    },
    {
        functions: [
            () => new Promise(res => setTimeout(() => res(1), 200)),
            () => new Promise((_, rej) => setTimeout(() => rej("Error"), 100))
        ],
        expected: { rejected: "Error" },
        shouldReject: true
    },
    {
        functions: [
            () => new Promise(res => setTimeout(() => res(4), 50)),
            () => new Promise(res => setTimeout(() => res(10), 150)),
            () => new Promise(res => setTimeout(() => res(16), 100))
        ],
        expected: { resolved: [4, 10, 16] },
        shouldReject: false
    },
    {
        functions: [],
        expected: { resolved: [] },
        shouldReject: false
    }
];

testCases.forEach(({ functions, expected, shouldReject }, i) => {
    promiseAll(functions)
        .then(result => {
            if (shouldReject) {
                console.log(`Test Case ${i + 1}: Failed ❌ (Expected rejection, but got resolution)`);
            } else {
                console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected.resolved) ? "Passed ✅" : "Failed ❌");
                console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected.resolved)}`);
            }
        })
        .catch(error => {
            if (!shouldReject) {
                console.log(`Test Case ${i + 1}: Failed ❌ (Expected resolution, but got rejection)`);
            } else {
                console.log(`Test Case ${i + 1}:`, error === expected.rejected ? "Passed ✅" : "Failed ❌");
                console.log(`Error: ${JSON.stringify(error)}, Expected: ${JSON.stringify(expected.rejected)}`);
            }
        });
});
