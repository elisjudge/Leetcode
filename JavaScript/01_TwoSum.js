/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function (nums, target) {
    let hashMap = {};
    let diff = 0;
    for (let i = 0; i < nums.length; i++) {
        diff = target - nums[i];
        if (diff in hashMap) {
            return [hashMap[diff], i];
        }
        hashMap[nums[i]] = i;
    }
    return [];
};

const testCases = [
    {
        nums: [2,7,11,15],
        target: 9,
        expected: [0, 1]
    },
    {
        nums: [3,2,4],
        target: 6,
        expected: [1, 2]
    },
    {
        nums: [3,3],
        target: 6,
        expected: [0, 1]
    }
]

testCases.forEach((testCase, i) => {
    const output = twoSum(testCase.nums, testCase.target);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});