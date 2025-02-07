/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const idMap = new Map();

    const mergeObjects = (obj1, obj2) => {
        return { ...obj1, ...obj2 };
    };

    [...arr1, ...arr2].forEach(obj => {
        if (idMap.has(obj.id)) {
            idMap.set(obj.id, mergeObjects(idMap.get(obj.id), obj));
        } else {
            idMap.set(obj.id, obj);
        }
    });

    return Array.from(idMap.values()).sort((a, b) => a.id - b.id);
};

const testCases = [
    {
        arr1: [{ id: 1, x: 1 }, { id: 2, x: 9 }],
        arr2: [{ id: 3, x: 5 }],
        expected: [
            { id: 1, x: 1 },
            { id: 2, x: 9 },
            { id: 3, x: 5 }
        ]
    },
    {
        arr1: [{ id: 1, x: 2, y: 3 }, { id: 2, x: 3, y: 6 }],
        arr2: [{ id: 2, x: 10, y: 20 }, { id: 3, x: 0, y: 0 }],
        expected: [
            { id: 1, x: 2, y: 3 },
            { id: 2, x: 10, y: 20 },
            { id: 3, x: 0, y: 0 }
        ]
    },
    {
        arr1: [{ id: 1, b: { b: 94 }, v: [4, 3], y: 48 }],
        arr2: [{ id: 1, b: { c: 84 }, v: [1, 3] }],
        expected: [
            { id: 1, b: { c: 84 }, v: [1, 3], y: 48 }
        ]
    },
    {
        arr1: [{ id: 4, name: "Alice" }],
        arr2: [{ id: 4, age: 30 }],
        expected: [
            { id: 4, name: "Alice", age: 30 }
        ]
    },
    {
        arr1: [],
        arr2: [],
        expected: []
    }
];

// Run the test cases
testCases.forEach(({ arr1, arr2, expected }, i) => {
    const result = join(arr1, arr2);
    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});
