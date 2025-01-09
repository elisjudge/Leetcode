/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const countS = {};
    const countT = {};

    for (let i = 0; i < s.length; i++) {
        countS[s[i]] = 1 + (countS[s[i]] ?? 0);
        countT[t[i]] = 1 + (countT[t[i]] ?? 0);
    }

    for (const char in countS) {
        if (countS[char] !== countT[char] ?? 0) {
            return false;
        }
    }
    return true;
};


const testCases = [
    {
        s: "anagram",
        t: "nagaram",
        expected: true
    },
    {
        s: "rat",
        t: "car",
        expected: false
    }
]

testCases.forEach((testCase, i) => {
    const output = isAnagram(testCase.s, testCase.t);
    if (output === testCase.expected) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});