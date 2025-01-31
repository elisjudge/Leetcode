/**
 * @return {null|boolean|number|string|Array|Object}
 */


Array.prototype.last = function() {
    if (this.length === 0 ) {
        return -1;
    }
    return this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */

const testCases = [
    { arr: new Array(), expected: -1 }, 
    { arr: new Array(null, {}, 3), expected: 3 },
    { arr: new Array(1).fill(42), expected: 42 },                      
    { arr: new Array("apple", "banana", "cherry"), expected: "cherry" },  
    { arr: new Array(1, 2, 3, 4, 5), expected: 5 },             
    { arr: new Array({ a: 1 }, true, false), expected: false }    
];

testCases.forEach(({ arr, expected }, i) => {
    const result = arr.last();
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});