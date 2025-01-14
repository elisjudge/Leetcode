/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = function(s, numRows) {
    if (numRows === 1) {
        return s;
    }

    const hashMap = {}
    let zig = true;
    let zag = false;
    let row = 0;
    let result = "";

    for (let i = 0; i < numRows; i++) {
        hashMap[i] = [];
    }

    for (let i = 0; i < s.length; i++) {
        if (zig) {
            hashMap[row].push(s[i]);
            if (row === numRows - 1) {
                zig = false;
                zag = true;
                row--;
            } else {
                row++;
            }
        } else if (zag) {
            hashMap[row].push(s[i])
            if (row === 0) {
                zig = true;
                zag = false;
                row++;
            } else {
                row--; 
            }
        }
    }

    for (let i = 0; i < numRows; i++) {
        hashMap[i].forEach(char => {
            result = result.concat('', char);
        })
    }
    
    return result;
};


testCases = [
    {
        s: "PAYPALISHIRING",
        numRows: 3,
        expected: "PAHNAPLSIIGYIR"
    },
    {
        s: "PAYPALISHIRING",
        numRows: 4,
        expected: "PINALSIGYAHRPI"
    },
    {
        s: "A",
        numRows: 1,
        expected: "A"
    },
    {
        s: "AB",
        numRows: 1,
        expected: "AB"
    },
    {
        s: "AB",
        numRows: 2,
        expected: "AB"
    },
]

testCases.forEach((testCase, i) => {
    const output = convert(testCase.s, testCase.numRows);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    }
    
});