/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i > -1; i--) {
        if (digits[i] < 9) {
            digits[i] += 1;
            return digits;
        }
        digits[i] = 0;
    }
    digits.unshift(1)
    return digits;
};


const testCases = [
    {
        digits: [1,2,3],
        expected: [1,2,4]
    },
    {
        digits: [1,2,3,4],
        expected: [1,2,3,5]
    },
    {
        digits: [9,9,9],
        expected: [1,0,0,0]
    },
    {
        digits: [4,3,2,1],
        expected: [4,3,2,2]
    },
    {
        digits: [9],
        expected: [1,0]
    },
]

testCases.forEach((testCase, i) => {
    const output = plusOne(testCase.digits);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});