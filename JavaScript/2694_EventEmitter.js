class EventEmitter {
    constructor() {
        this.eventListeners = {};
    }
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.eventListeners[eventName]) {
            this.eventListeners[eventName] = [];
        }

        this.eventListeners[eventName].push(callback);
        
        return {
            unsubscribe: () => {
                this.eventListeners[eventName] = this.eventListeners[eventName].filter(fn => fn !== callback);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (!this.eventListeners[eventName]) {
            return [];
        }

        return this.eventListeners[eventName].map(fn => fn(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */


const testCases = [
    {
        actions: ["EventEmitter", "emit", "subscribe", "subscribe", "emit"],
        values: [[], ["firstEvent"], ["firstEvent", () => 5], ["firstEvent", () => 6], ["firstEvent"]],
        expected: [[], [], "subscribed", "subscribed", [5, 6]]
    },
    {
        actions: ["EventEmitter", "subscribe", "emit", "emit"],
        values: [[], ["event", (...args) => args.join(",")], ["event", [1, 2, 3]], ["event", [4, 5, 6]]],
        expected: [[], "subscribed", ["1,2,3"], ["4,5,6"]]
    },
    {
        actions: ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"],
        values: [[], ["event", (...args) => args.join(",")], ["event", [1, 2, 3]], [0], ["event", [4, 5, 6]]],
        expected: [[], "subscribed", ["1,2,3"], "unsubscribed", []]
    },
    {
        actions: ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"],
        values: [[], ["event", x => x + 1], ["event", x => x + 2], [0], ["event", [5]]],
        expected: [[], "subscribed", "subscribed", "unsubscribed", [7]]
    }
];

// Run the test cases
testCases.forEach(({ actions, values, expected }, i) => {
    const emitter = new EventEmitter();
    const subscriptions = [];  // Store subscriptions for later access
    let result = [];

    actions.forEach((action, index) => {
        if (action === "EventEmitter") {
            result.push([]);
        } else if (action === "subscribe") {
            const [eventName, callback] = values[index];
            const subscription = emitter.subscribe(eventName, callback);
            subscriptions.push(subscription);  // Store subscription for future unsubscribe
            result.push("subscribed");
        } else if (action === "emit") {
            const [eventName, args] = values[index];
            result.push(emitter.emit(eventName, args || []));
        } else if (action === "unsubscribe") {
            const subscriptionIndex = values[index][0];
            if (subscriptions[subscriptionIndex]) {
                subscriptions[subscriptionIndex].unsubscribe();
                result.push("unsubscribed");
            }
        }
    });

    console.log(`Test Case ${i + 1}:`, JSON.stringify(result) === JSON.stringify(expected) ? "Passed ✅" : "Failed ❌");
    console.log(`Result: ${JSON.stringify(result)}, Expected: ${JSON.stringify(expected)}`);
});

