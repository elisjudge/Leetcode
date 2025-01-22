/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

class MinHeap {
    constructor() {
        this.heap = [];
    }

    // Swap elements in the heap
    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    // Get the index of the parent node
    parentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    // Get the index of the left child node
    leftChildIndex(index) {
        return 2 * index + 1;
    }

    // Get the index of the right child node
    rightChildIndex(index) {
        return 2 * index + 2;
    }

    // Add an element to the heap
    push(element) {
        this.heap.push(element);
        this.bubbleUp();
    }

    // Remove and return the smallest element (root) from the heap
    pop() {
        if (this.heap.length === 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown();
        return root;
    }

    // Return the smallest element (root) without removing it
    peek() {
        return this.heap[0];
    }

    // Bubble up the last element to maintain heap property
    bubbleUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parent = this.parentIndex(index);
            if (this.heap[index][0] >= this.heap[parent][0]) break;
            this.swap(index, parent);
            index = parent;
        }
    }

    // Bubble down the root element to maintain heap property
    bubbleDown() {
        let index = 0;
        const length = this.heap.length;

        while (true) {
            const left = this.leftChildIndex(index);
            const right = this.rightChildIndex(index);
            let smallest = index;

            if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                smallest = left;
            }
            if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                smallest = right;
            }
            if (smallest === index) break;

            this.swap(index, smallest);
            index = smallest;
        }
    }

    // Return the size of the heap
    size() {
        return this.heap.length;
    }
}

const topKFrequent_Heap = function(nums, k) {
    const frequencies = new Map();
    const heap = new MinHeap();
    const result = []
    
    for (const num of nums) {
        frequencies.set(num, (frequencies.get(num) || 0) + 1);
    }

    for (const [num, freq] of frequencies) {
        if (heap.size() < k) {
            heap.push([freq, num]);
        } else if (freq > heap.peek()[0]) {
            heap.pop();
            heap.push([freq, num]);
        }
    }

    while (heap.size() > 0) {
        result.push(heap.pop()[1]);
    }

    return result.reverse();
};

const topKFrequent_Bucket = function(nums, k) {
    const frequencies = new Map();
    const value_arrays = Array.from({length: nums.length +1}, () => []);
    const result = [];

    for (const num of nums) {
        frequencies.set(num, (frequencies.get(num) || 0) + 1);
    }
    for (const [num, freq] of frequencies) {
        value_arrays[freq].push(num);
    }

    for (let i = nums.length; i >= 0; i--) {
        for (const num of value_arrays[i]) {
            result.push(num);
        }
        if (result.length === k) {
            return result;
        }
    }
};

const testCases = [
    {
        nums: [1],
        k: 1,
        expected: [1]
    },
    {
        nums: [1,1,1,2,2,3],
        k: 2,
        expected: [1,2]
    },
]

testCases.forEach((testCase, i) => {
    const output_bucket = topKFrequent_Bucket(testCase.nums, testCase.k);
    const output_heap = topKFrequent_Heap(testCase.nums, testCase.k);

    if (JSON.stringify(output_bucket) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output (Bucket): ${JSON.stringify(output_bucket)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output (Bucket): ${JSON.stringify(output_bucket)} `)
    }

    if (JSON.stringify(output_heap) === JSON.stringify(testCase.expected)) {
        console.log(`Test Case ${i}: Passed. Expected: ${JSON.stringify(testCase.expected)}, Output (Heap): ${JSON.stringify(output_heap)} `)
    } else {
        console.log(`Test Case ${i}: Failed. Expected: ${JSON.stringify(testCase.expected)}, Output (Heap): ${JSON.stringify(output_heap)} `)
    }
});