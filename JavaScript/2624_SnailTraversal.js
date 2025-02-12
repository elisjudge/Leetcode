/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    const nums = this;
    if (rowsCount * colsCount !== nums.length) return [];

    const result = Array.from({ length: rowsCount }, () => []);

    let index = 0;

    for (let col = 0; col < colsCount; col++) {
        if (col % 2 === 0) {
        
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = nums[index++];
            }
        } else {
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = nums[index++];
            }
        }
    }

    return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */


const testCases = [
    {
        nums: [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15],
        rowsCount: 5,
        colsCount: 4,
        expected: [
            [19, 17, 16, 15],
            [10,  1, 14,  4],
            [ 3,  2, 12, 20],
            [ 7,  5, 18, 11],
            [ 9,  8,  6, 13]
        ]
    },
    {
        nums: [1, 2, 3, 4],
        rowsCount: 1,
        colsCount: 4,
        expected: [[1, 2, 3, 4]]
    },
    {
        nums: [1, 3],
        rowsCount: 2,
        colsCount: 2,
        expected: []
    },
    {
        nums: [],
        rowsCount: 1,
        colsCount: 1,
        expected: []
    }
];

// Run test cases
testCases.forEach(({ nums, rowsCount, colsCount, expected }, i) => {
    const arr = nums.slice(); // Copy to avoid mutation
    const result = arr.snail(rowsCount, colsCount);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});