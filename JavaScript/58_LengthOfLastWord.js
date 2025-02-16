/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let i = s.length - 1;
    let count = 0;
    while (s[i] === " ") {
        i--;
    }

    while (i >= 0 && s[i] !== " ") {
        count ++;
        i--;
    }

    return count;
};


const testCases = [
    {
        s: "Hello World",
        expected: 5
    },
    {
        s: "   fly me   to   the moon  ",
        expected: 4
    },
    {
        s: "luffy is still joyboy",
        expected: 6
    },
]

testCases.forEach((testCase, i) => {
    const output = lengthOfLastWord(testCase.s);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});