class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.result = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        this.result += value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        this.result -= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        this.result *= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed")
        }
        this.result /= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.result = Math.pow(this.result, value);
        return this;
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.result;
    }
}

const testCases = [
    { actions: ["Calculator", "add", "subtract", "getResult"], values: [10, 5, 7], expected: 8 },
    { actions: ["Calculator", "multiply", "power", "getResult"], values: [2, 5, 2], expected: 100 },
    { actions: ["Calculator", "divide", "getResult"], values: [20, 0], expected: "Division by zero is not allowed" }
];

testCases.forEach(({ actions, values, expected }, i) => {
    try {
        let calculator;

        actions.forEach((action, index) => {
            if (action === "Calculator") {
                calculator = new Calculator(values[index]);
            } else if (action === "getResult") {
                const result = calculator.getResult();
                console.log(`Test Case ${i + 1}:`, Math.abs(result - expected) < 1e-5 ? "Passed ✅" : "Failed ❌");
                console.log(`Result: ${result}, Expected: ${expected}`);
            } else {
                calculator[action](values[index]);
            }
        });
    } catch (error) {
        console.log(`Test Case ${i + 1}:`, error.message === expected ? "Passed ✅" : "Failed ❌");
        console.log(`Error: ${error.message}, Expected: ${expected}`);
    }
});
