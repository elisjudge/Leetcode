/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((sum, num) => sum + num, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(',')}]`;
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */

const testCases = [
    { arr: [1, 2], operation: 'Add', otherArr: [3, 4], expected: 10 },             
    { arr: [23, 98, 42, 70], operation: 'String', expected: '[23,98,42,70]' },     
    { arr: [], operation: 'Add', otherArr: [], expected: 0 },                      
    { arr: [-5, -10, -15], operation: 'Add', otherArr: [5, 10], expected: -15 },   
    { arr: [42], operation: 'String', expected: '[42]' }                           
];

testCases.forEach(({ arr, operation, otherArr, expected }, i) => {
    let result;
    
    if (operation === 'Add') {
        const obj1 = new ArrayWrapper(arr);
        const obj2 = new ArrayWrapper(otherArr);
        result = obj1 + obj2;  
    } else if (operation === 'String') {
        const obj = new ArrayWrapper(arr);
        result = String(obj); 
    }

    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});