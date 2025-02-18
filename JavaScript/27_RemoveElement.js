/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
};

const testCases = [
    {
        nums: [3,2,2,3],
        val: 3,
        expected: 2
    },
    {
        nums: [0,1,2,2,3,0,4,2],
        val: 2,
        expected: 5
    }
]


testCases.forEach((testCase, i) => {
    const output = removeElement(testCase.nums, testCase.val);
    if (output === testCase.expected) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});