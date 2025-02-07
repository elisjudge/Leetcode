/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj
            .map(compactObject)
            .filter(Boolean);
    }

    if (obj !== null && typeof obj === "object") {
        const result = {};
        for (const key in obj) {
            const compactedValue = compactObject(obj[key]);
            if (Boolean(compactedValue)) {
                result[key] = compactedValue;
            }
        }
        return result;
    }

    return obj;
};

const testCases = [
    {
        obj: [null, 0, false, 1],
        expected: [1]
    },
    {
        obj: { a: null, b: [false, 1] },
        expected: { b: [1] }
    },
    {
        obj: [null, 0, 5, [0], [false, 16]],
        expected: [5, [], [16]]
    },
    {
        obj: { x: 0, y: null, z: { a: 0, b: false, c: 3 } },
        expected: { z: { c: 3 } }
    },
    {
        obj: [],
        expected: []
    },
    {
        obj: {},
        expected: {}
    }
];

// Run the test cases
testCases.forEach(({ obj, expected }, i) => {
    const result = compactObject(obj);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
