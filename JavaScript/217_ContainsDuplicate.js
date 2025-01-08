/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function(nums) {
    const hashSet = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (hashSet.has(nums[i])) {
            return true;
        }
        hashSet.add(nums[i]);
    }

    return false;
};

const testCases = [
    {
        nums: [1,2,3,1],
        expected: true
    },
    {
        nums: [1,2,3,4],
        expected: false
    },
    {
        nums: [1,1,1,3,3,4,3,2,4,2],
        expected: true
    }
]

testCases.forEach((testCase, i) => {
    const output = containsDuplicate(testCase.nums);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});