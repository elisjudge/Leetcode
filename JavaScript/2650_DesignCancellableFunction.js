/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = (generator) => {
    let cancel;
    const cancelPromise = new Promise((_, reject) => {
        cancel = () => reject("Cancelled");
    });

    // Prevent unhandled promise rejection
    cancelPromise.catch(() => {});

    const promise = (async () => {
        let next = generator.next();
        while (!next.done) {
            try {
                next = generator.next(await Promise.race([next.value, cancelPromise]));
            } catch (e) {
                next = generator.throw(e);
            }
        }
        return next.value;
    })();

    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */

// Define the test cases
const testCases = [
    {
        generatorFunction: function*() { 
            return 42; 
        },
        cancelledAt: 100,
        expected: { resolved: 42 }
    },
    {
        generatorFunction: function*() {
            const msg = yield new Promise(res => res("Hello"));
            throw `Error: ${msg}`;
        },
        cancelledAt: null,
        expected: { rejected: "Error: Hello" }
    },
    {
        generatorFunction: function*() {
            yield new Promise(res => setTimeout(res, 200));
            return "Success";
        },
        cancelledAt: 100,
        expected: { rejected: "Cancelled" }
    },
    {
        generatorFunction: function*() {
            let result = 0;
            yield new Promise(res => setTimeout(res, 100));
            result += yield new Promise(res => res(1));
            yield new Promise(res => setTimeout(res, 100));
            result += yield new Promise(res => res(1));
            return result;
        },
        cancelledAt: null,
        expected: { resolved: 2 }
    },
    {
        generatorFunction: function*() {
            let result = 0;
            try {
                yield new Promise(res => setTimeout(res, 100));
                result += yield new Promise(res => res(1));
                yield new Promise(res => setTimeout(res, 100));
                result += yield new Promise(res => res(1));
            } catch (e) {
                return result;
            }
            return result;
        },
        cancelledAt: 150,
        expected: { resolved: 1 }
    },
    {
        generatorFunction: function*() {
            try {
                yield new Promise((_, reject) => reject("Promise Rejected"));
            } catch (e) {
                let a = yield new Promise(resolve => resolve(2));
                let b = yield new Promise(resolve => resolve(2));
                return a + b;
            }
        },
        cancelledAt: null,
        expected: { resolved: 4 }
    }
];

// Function to run test cases
testCases.forEach(({ generatorFunction, cancelledAt, expected }, i) => {
    const generator = generatorFunction();
    const [cancel, promise] = cancellable(generator);

    if (cancelledAt !== null) {
        setTimeout(cancel, cancelledAt);
    }

    promise
        .then(result => {
            const output = { resolved: result };
            console.log(`Test Case ${i + 1}:`, JSON.stringify(output) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
            console.log(`Result: ${JSON.stringify(output)}, Expected: ${JSON.stringify(expected)}`);
        })
        .catch(error => {
            const output = { rejected: error };
            console.log(`Test Case ${i + 1}:`, JSON.stringify(output) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
            console.log(`Result: ${JSON.stringify(output)}, Expected: ${JSON.stringify(expected)}`);
        });
});
