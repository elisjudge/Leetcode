/**
 * @param {number} num
 * @return {string}
 */
const intToRoman = function(num) {
    const letterValues =  new Map([
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
    ]);
    let roman = "";

    for (const [key, value] of letterValues) {
        while ((num / value) >= 1) {
            roman += key;
            num -= value;
        }
    }
    return roman;
};

const testCases = [
    {
        num: 3749,
        expected: "MMMDCCXLIX"
    },
    {
        num: 1469,
        expected: "MCDLXIX"
    },
    {
        num: 58,
        expected: "LVIII"
    },
    {
        num: 1994,
        expected: "MCMXCIV"
    },
]

testCases.forEach((testCase, i) => {
    const output = intToRoman(testCase.num);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
})