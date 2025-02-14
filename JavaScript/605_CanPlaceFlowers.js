/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    const f = [0, ...flowerbed, 0]

    for (let i = 1; i < f.length - 1; i++) {
        if (f[i - 1] === 0 && f[i] === 0 && f[i + 1] === 0) {
            f[i] = 1;
            n--;
        }
    }
    
    return n <= 0;
};

const testCases = [
    {
        flowerbed: [1,0,0,0,1],
        n: 1,
        expected: true
    },
    {
        flowerbed: [1,0,0,0,1],
        n: 2,
        expected: false
    }
]

testCases.forEach((testCase, i) => {
    const output = canPlaceFlowers(testCase.flowerbed, testCase.n);
    if (JSON.stringify(output) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)} `)
    } 
});