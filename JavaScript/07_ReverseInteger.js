/**
 * @param {number} x
 * @return {number}
 */
const reverse = function(x) {
    let negative = false;
    let revNum = 0;

    if (x < 0) {
        negative = true;
        x = Math.abs(x);
    }
    
    while (x > 0) {
        let lastDigit = x % 10;
        revNum = revNum * 10 + lastDigit;
        x = Math.floor(x / 10); 
    }

    if (revNum > (2**31 - 1)) {
        return 0;
    }
    
    return negative ? -revNum : revNum;
};

const testCases = [
    {
        x: -1234,
        expected: -4321
    },
    {
        x: 1534236469,
        expected: 0
    },
    {
        x: 123,
        expected: 321
    },
    {
        x: 120,
        expected: 21
    }
]

testCases.forEach((testCase, i) => {
    const output = reverse(testCase.x);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});