/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function (context, ...args) {
    const tempKey = Symbol(); 
    context[tempKey] = this;  
    const result = context[tempKey](...args); 
    delete context[tempKey]; 
    return result; 
};


/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */

const testCases = [
    {
        fn: function add(b) {
            return this.a + b;
        },
        args: [{ "a": 5 }, 7],
        expected: 12
    },
    {
        fn: function tax(price, taxRate) {
            return `The cost of the ${this.item} is ${price * taxRate}`;
        },
        args: [{ "item": "burger" }, 10, 1.1],
        expected: "The cost of the burger is 11"
    },
    {
        fn: function increment() {
            this.count++;
            return this.count;
        },
        args: [{ "count": 1 }],
        expected: 2
    },
    {
        fn: function greeting(name) {
            return `Hello ${name}, welcome to ${this.company}!`;
        },
        args: [{ "company": "OpenAI" }, "Alice"],
        expected: "Hello Alice, welcome to OpenAI!"
    },
    {
        fn: function multiply(x, y) {
            return this.factor * x * y;
        },
        args: [{ "factor": 2 }, 3, 4],
        expected: 24
    }
];

// Run test cases
testCases.forEach(({ fn, args, expected }, i) => {
    const result = fn.callPolyfill(...args);
    console.log(`Test Case ${i + 1}:`, result === expected ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
