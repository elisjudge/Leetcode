/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
};

const testCases = [
    { arr: [1,2,3,4,5], size: 1, expected: [[1],[2],[3],[4],[5]] },
    { arr: [1,9,6,3,2], size: 3, expected: [[1,9,6], [3,2]] },
    { arr: [8,5,3,2,6], size: 6, expected: [[8,5,3,2,6]] },
    { arr: [], size: 1, expected: [] },
    { arr: [1,2,3,4,5,6,7,8,9,10], size: 4, expected: [[1,2,3,4], [5,6,7,8], [9,10]] }
];

testCases.forEach(({ arr, size, expected }, i) => {
    const result = chunk(arr, size);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
