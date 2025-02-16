/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;
    let m;

    if (target > nums[r]) {
        return r + 1;
    } else if (target < nums[l]) {
        return l;
    }

    while (l <= r) {
        m = Math.floor((l + r) / 2);
        if (nums[m] > target) {
            r = m - 1;
        } else if (nums[m] < target) {
            l = m + 1
        } else {
            return m;
        }
    }

    return l;
};

const testCases = [
    {
        nums: [1,3,5,6],
        target: 5,
        expected: 2
    },
    {
        nums: [1,3,5,6],
        target: 2,
        expected: 1
    },
    {
        nums: [1,3,5,6],
        target: 7,
        expected: 4
    },
]

testCases.forEach((testCase, i) => {
    const output = searchInsert(testCase.nums, testCase.target);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});