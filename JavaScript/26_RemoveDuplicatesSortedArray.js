/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let n = nums.length;
    if (n === 1) {
        return 1;
    }
    
    let l = 0;
    let r = 1;
    let k = 1;

    while (r < n) {
        if (nums[l] == nums[r]) {
            r++;
        } else {
            nums[k] = nums[r]
            k++;
            l = r;
            r++;
        }
    }
    return k;    
};

const testCases = [
    {
        nums: [1,1,2],
        expected: 2
    },
    {
        nums: [0,0,1,1,1,2,2,3,3,4],
        expected: 5
    }
]

testCases.forEach((testCase, i) => {
    const output = removeDuplicates(testCase.nums);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});