/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = function(strs) {
    const hashMap = new Map();

    strs.forEach(str => {
        const count = new Array(26).fill(0);

        for (let i = 0; i < str.length; i++) {
            count[str[i].codePointAt(0) - "a".codePointAt(0)]++;
        }

        const key = count.join(',');

        if (!hashMap.has(key)) {
            hashMap.set(key, [str]);
        } else {
            hashMap.get(key).push(str);
        }
    })

    return Array.from(hashMap.values());
};

function areAnagramGroupsEqual(arr1, arr2) {
    const sortedArr1 = arr1.map(subArr => subArr.sort()).sort();
    const sortedArr2 = arr2.map(subArr => subArr.sort()).sort();

    return JSON.stringify(sortedArr1) === JSON.stringify(sortedArr2);
}


const testCases = [
    {
        strs: ["eat","tea","tan","ate","nat","bat"],
        expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
    },
    {
        strs: [""],
        expected: [[""]]
    },
    {
        strs: ["a"],
        expected: [["a"]]
    }
]

testCases.forEach((testCase, i) => {
    const output = groupAnagrams(testCase.strs);
    if (areAnagramGroupsEqual(output, testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `);
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `);
    }
});