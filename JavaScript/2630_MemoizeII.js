/**
 * Trie-based Memoization Solution
 */
class LookupTree {
    constructor() {
        this.map = new Map(); // Stores child nodes for arguments
        this.hasValue = false; // Indicates if this node holds a cached value
        this.value = null; // Stores the function result
    }

    getValueHelper(path, i) {
        if (i >= path.length) {
            return this.hasValue ? { value: this.value, success: true } : { success: false };
        }
        const key = path[i];
        if (this.map.has(key)) {
            return this.map.get(key).getValueHelper(path, i + 1);
        }
        return { success: false };
    }

    getValue(path) {
        return this.getValueHelper(path, 0);
    }

    setValueHelper(path, i, value) {
        if (i >= path.length) {
            this.value = value;
            this.hasValue = true;
            return;
        }
        const key = path[i];
        if (!this.map.has(key)) {
            this.map.set(key, new LookupTree());
        }
        this.map.get(key).setValueHelper(path, i + 1, value);
    }

    setValue(path, value) {
        this.setValueHelper(path, 0, value);
    }
}

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const tree = new LookupTree();
    
    return function (...args) {
        const cache = tree.getValue(args);
        if (cache.success) {
            return cache.value;
        }

        const result = fn(...args);
        tree.setValue(args, result);
        return result;
    };
}



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */


 /**
 * Example function for memoization
 */
let callCount = 0;
const add = (a, b) => {
    callCount += 1;
    return a + b;
};

/**
 * Memoized version
 */
const memoizedAdd = memoize(add);

const testCases = [
    {
        inputs: [2, 3],
        expected: 5
    },
    {
        inputs: [2, 3],
        expected: 5 // Should return cached result
    },
    {
        inputs: [1, 3],
        expected: 4
    },
    {
        inputs: [1, 3],
        expected: 4 // Should return cached result
    },
    {
        inputs: ["hello", "world"],
        expected: "helloworld"
    },
    {
        inputs: ["hello", "world"],
        expected: "helloworld" // Should return cached result
    },
    {
        inputs: [null, undefined],
        expected: null
    }
];

// Run test cases
testCases.forEach(({ inputs, expected }, i) => {
    const result = memoizedAdd(...inputs);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});

console.log(`Function Calls: ${callCount}`); // Should be <= unique calls
