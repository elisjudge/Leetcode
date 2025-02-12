/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */

var checkIfInstanceOf = function(obj, classFunction) {
    if (classFunction === null || classFunction === undefined || typeof classFunction !== "function") {
        return false;
    }

    // Explicitly handle null and undefined
    if (obj === null || obj === undefined) {
        return false;
    }

    // If obj has no prototype, it must be a primitive (except for Object.create(null))
    if (Object.getPrototypeOf(obj) === null) {
        return false;
    }

    // Handle primitives by wrapping them
    if (typeof obj !== "object" && typeof obj !== "function") {
        return Object(obj) instanceof classFunction;
    }

    // Check prototype chain manually for objects
    let proto = Object.getPrototypeOf(obj);
    while (proto !== null) {
        if (proto.constructor === classFunction) {
            return true;
        }
        proto = Object.getPrototypeOf(proto);
    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */

const testCases = [
    {
        obj: new Date(),
        classFunction: Date,
        expected: true
    },
    {
        obj: Date,
        classFunction: Date,
        expected: false
    },
    {
        obj: new (class Animal {})(),
        classFunction: Object,
        expected: true
    },
    {
        obj: new (class Dog extends (class Animal {}) {})(),
        classFunction: Object,
        expected: true
    },
    {
        obj: 5,
        classFunction: Number,
        expected: true
    },
    {
        obj: "hello",
        classFunction: String,
        expected: true
    },
    {
        obj: true,
        classFunction: Boolean,
        expected: true
    },
    {
        obj: null,
        classFunction: Object,
        expected: false
    },
    {
        obj: undefined,
        classFunction: Object,
        expected: false
    },
    {
        obj: [],
        classFunction: Array,
        expected: true
    },
    {
        obj: {},
        classFunction: Object,
        expected: true
    },
    {
        obj: function () {},
        classFunction: Function,
        expected: true
    },
    {
        obj: new Map(),
        classFunction: Object,
        expected: true
    },
    {
        obj: new Set(),
        classFunction: Set,
        expected: true
    }
];

// Run the test cases
testCases.forEach(({ obj, classFunction, expected }, i) => {
    const result = checkIfInstanceOf(obj, classFunction);
    console.log(`Test Case ${i + 1}:`, result === expected ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${result}, Expected: ${expected}`);
});
