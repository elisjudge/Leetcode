/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let end = m + n - 1;

    while (m > 0 && n > 0) {
        if (nums1[m - 1] >= nums2[n - 1]) {
            nums1[end] = nums1[m - 1];
            m--;
        } else {
            nums1[end] = nums2[n - 1]
            n--;
        }
        end--;
    }

    while (n > 0) {
        nums1[end] = nums2[n - 1];
        n--;
        end--;
    }
};

const testCases = [
    {
        nums1: [1,2,3,0,0,0],
        m: 3,
        nums2: [2,5,6],
        n: 3,
        expected: [1,2,2,3,5,6]
    },
    {
        nums1: [1],
        m: 1,
        nums2: [],
        n: 0,
        expected: [1]
    },
    {
        nums1: [0],
        m: 0,
        nums2: [1],
        n: 1,
        expected: [1]
    },
]

testCases.forEach((testCase, i) => {
    const output = testCase.nums1;
    merge(output, testCase.m, testCase.nums2, testCase.n);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});