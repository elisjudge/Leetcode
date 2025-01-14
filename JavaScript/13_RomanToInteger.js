/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = function(s) {
    const letterValues = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };
    const reverseS = s.split('').reverse();
    let total = 0;

    reverseS.forEach(letter => {
       total += letterValues[letter];
       if (letter === "I" && total >= 5) {
           total -= 2;     
       } else if (letter === "X" && total >= 50) {
           total -= 20;
       } else if (letter === "C" && total >= 500) {
           total -= 200;
       }
    })
    return total;
}; 

const testCases = [
    {
        s: "III",
        expected: 3
    },
    {
        s: "LVIII",
        expected: 58
    },
    {
        s: "MCMXCIV",
        expected: 1994
    },
]

testCases.forEach((testCase, i) => {
    const output = romanToInt(testCase.s);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
})