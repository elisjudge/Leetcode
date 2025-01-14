/**
 * @param {string} s
 * @return {number}
 */

const lengthOfLongestSubstring = function(s) {
    let result = 0;
    let l = 0;
    const unique_chars = new Set();
    
    for (let r = 0; r < s.length; r++) {
        while (unique_chars.has(s[r])) {
            unique_chars.delete(s[l]);
            l++;
        }
        unique_chars.add(s[r]);
        const currentSubstringLength = unique_chars.size;
        result = Math.max(result, currentSubstringLength);
    }

    return result;
};


const testCases = [
    {
        s: "abcabcbb",
        expected: 3
    },
    {
        s: "bbbbb",
        expected: 1
    },
    {
        s: "pwwkew",
        expected: 3
    },
    {
        s: "",
        expected: 0
    },
    {
        s: " ",
        expected: 1
    },
    {
        s: "dvdf",
        expected: 3
    }
]

testCases.forEach((testCase, i) => {
    const output = lengthOfLongestSubstring(testCase.s);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
});