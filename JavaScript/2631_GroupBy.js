/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const result = {};

    for (const item of this) {
        const key = fn(item);
        if (!result[key]) {
            result[key] = [];
        }
    
        result[key].push(item);
    }
    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */


const testCases = [
    {
        arr: [1, 2, 3], 
        fn: String, 
        expected: { "1": [1], "2": [2], "3": [3] }
    },
    {
        arr: [
            { id: "1" }, 
            { id: "1" }, 
            { id: "2" }
        ],
        fn: (item) => item.id,
        expected: { "1": [{ id: "1" }, { id: "1" }], "2": [{ id: "2" }] }
    },
    {
        arr: [
            [1, 2, 3], 
            [1, 3, 5], 
            [2, 5, 9]
        ],
        fn: (list) => String(list[0]),
        expected: { "1": [[1, 2, 3], [1, 3, 5]], "2": [[2, 5, 9]] }
    },
    {
        arr: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        fn: (n) => String(n > 5),
        expected: { "false": [1, 2, 3, 4, 5], "true": [6, 7, 8, 9, 10] }
    },
    {
        arr: [],
        fn: (x) => x,
        expected: {}
    }
];

testCases.forEach(({ arr, fn, expected }, i) => {
    const result = arr.groupBy(fn);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
