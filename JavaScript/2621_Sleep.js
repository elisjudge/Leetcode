/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve => {
        setTimeout(() => resolve(millis), millis);
    });
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

const testCases = [
    { millis: 50, expected: 50 },
    { millis: 100, expected: 100 },
    { millis: 200, expected: 200 },
    { millis: 500, expected: 500 },
    { millis: 1000, expected: 1000 }
];

testCases.forEach((testCase, i) => {
    let t = Date.now();
    sleep(testCase.millis).then(() => {
        let elapsedTime = Date.now() - t;
        // Allowing slight variations due to system scheduling delays
        if (Math.abs(elapsedTime - testCase.expected) <= 20) {
            console.log(`Test Case ${i}: Passed. Expected: ${testCase.expected}, Elapsed Time: ${elapsedTime}`);
        } else {
            console.log(`Test Case ${i}: Failed. Expected: ${testCase.expected}, Elapsed Time: ${elapsedTime}`);
        }
    }).catch(error => {
        console.log(`Test Case ${i}: Failed with error ${error}`);
    });
});