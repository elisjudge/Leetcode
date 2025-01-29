/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }
    return Object.keys(obj).length === 0;
};

const testCases = [
    { obj: {"x": 5, "y": 42}, expected: false },
    { obj: {}, expected: true },
    { obj: [null, false, 0], expected: false },
    { obj: [], expected: true },
    { obj: [1,2,3], expected: false },
    { obj: {"a": 1}, expected: false }
];

testCases.forEach(({ obj, expected }, i) => {
    const result = isEmpty(obj);
    console.log(`Test Case ${i + 1}:`, result === expected ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});