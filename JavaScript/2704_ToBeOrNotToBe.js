/**
 * @param {string} val
 * @return {Object}
 */
const expect = function(val) {
    const expectedVal = val;

    return {
        toBe: (val) => {
            if (val === expectedVal) {
                return true;
            } else {
                throw Error("Not Equal");
            }
        },
        notToBe: (val) => {
            if (val !== expectedVal) {
                return true;
            } else {
                throw Error("Equal");
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

const testCases = [
    {
        val: 5,
        calls: [
            { method: "toBe", argument: 5, throws: false, expected: true },
            { method: "notToBe", argument: 10, throws: false, expected: true },
        ],
    },
    {
        val: "hello",
        calls: [
            { method: "toBe", argument: "hello", throws: false, expected: true },
            { method: "notToBe", argument: "world", throws: false, expected: true },
            { method: "toBe", argument: "world", throws: true, expected: "Not Equal" },
        ],
    },
    {
        val: true,
        calls: [
            { method: "toBe", argument: true, throws: false, expected: true },
            { method: "notToBe", argument: false, throws: false, expected: true },
            { method: "notToBe", argument: true, throws: true, expected: "Equal" },
        ],
    },
]

testCases.forEach((testCase, i) => {
    const instance = expect(testCase.val);
    testCase.calls.forEach((call, j) => {
        try {
            const output = instance[call.method](call.argument);
            if (!call.trows && output === call.expected) {
                console.log(`Test Case ${i}-${j}: Passed. Expected: ${call.expected}, Output: ${output}`);
            } else {
                console.log(`Test Case ${i}-${j}: Failed. Expected: ${call.expected}, Output: ${output}`);
            }
        } catch (e) {
            if (call.throws && e.message === call.expected) {
                console.log(`Test Case ${i}-${j}: Passed. Expected Error: "${call.expected}", Caught: "${e.message}"`);
            } else {
                console.log(`Test Case ${i}-${j}: Failed. Expected Error: "${call.expected}", Caught: "${e.message}"`);
            }
        }
    }); 
});