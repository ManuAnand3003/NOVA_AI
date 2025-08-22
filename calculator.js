// calculator.js
const math = require('mathjs');

process.stdin.on('data', (data) => {
    const expression = data.toString().trim();
    try {
        const result = math.evaluate(expression);
        process.stdout.write(result.toString());
    } catch (e) {
        process.stdout.write(`Error: ${e.message}`);
    }
});