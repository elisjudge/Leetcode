/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const value1 = await promise1;
    const value2 = await promise2;
    return value1 + value2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

const testCases = [
    {
        promise1: new Promise(resolve => setTimeout(() => resolve(2), 20)),
        promise2: new Promise(resolve => setTimeout(() => resolve(3), 60)),
        expected: 5
    },
    {
        promise1: new Promise(resolve => setTimeout(() => resolve(10), 50)),
        promise2: new Promise(resolve => setTimeout(() => resolve(-12), 30)),
        expected: -2
    },
    {
        promise1: new Promise(resolve => setTimeout(() => resolve(0), 50)),
        promise2: new Promise(resolve => setTimeout(() => resolve(0), 50)),
        expected: 0
    },
    {
        promise1: new Promise(resolve => setTimeout(() => resolve(100), 10)),
        promise2: new Promise(resolve => setTimeout(() => resolve(200), 60)),
        expected: 300
    },
    {
        promise1: new Promise(resolve => setTimeout(() => resolve(-5), 90)),
        promise2: new Promise(resolve => setTimeout(() => resolve(-10), 25)),
        expected: -15
    }
];

testCases.forEach((testCase, i) => {
    addTwoPromises(testCase.promise1, testCase.promise2).then(output => {
        if (output === testCase.expected) {
            console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)}`);
        } else {
            console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output: ${JSON.stringify(output)}`);
        }
    }).catch(error => {
        console.log(`Test Case ${i}: Failed with error ${error}`);
    });
});