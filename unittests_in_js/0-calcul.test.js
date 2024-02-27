const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  // Test the basic functionality with whole numbers
  it('should return the sum of rounded a and b', function() {
    assert.strictEqual(calculateNumber(1, 3), 4); // Simple addition with no rounding needed
  });

  // Test rounding up one number and rounding down the other
  it('should return the sum when one is rounded up and the other is rounded down', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5); // 3.7 rounds up to 4
  });

  // Test rounding up both numbers
  it('should return the sum when both are rounded up', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5); // 1.2 rounds to 1 and 3.7 rounds to 4
  });

  // Test handling of rounding up to the nearest integer
  it('should handle rounding up to the next integer correctly', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6); // 1.5 rounds to 2 and 3.7 rounds to 4
  });

  // Test the function with negative numbers
  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1, -2), -3); // Negative numbers are rounded and added
    assert.strictEqual(calculateNumber(-1.4, 2.6), 2); // -1.4 rounds to -1 and 2.6 rounds to 3
  });

  // Test the function with both numbers being decimals
  it('should return the sum when both numbers are decimals', function() {
    assert.strictEqual(calculateNumber(0.1, 0.2), 0); // Both 0.1 and 0.2 round to 0
    assert.strictEqual(calculateNumber(0.9, 1.1), 2); // 0.9 rounds to 1 and 1.1 rounds to 1
  });

  // Test the function when the second number rounds to 0
  it('should return the first number when the second one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(1.2, 0.49), 1); // 0.49 rounds to 0, so result is 1.2 rounded
  });

  // Test the function when the first number rounds to 0
  it('should return the second number when the first one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(0.49, 2.5), 3); // 0.49 rounds to 0, so result is 2.5 rounded
  });

  // Test the function with zero values
  it('should handle zero correctly', function() {
    assert.strictEqual(calculateNumber(0, 0), 0); // Both zeros, expect 0
    assert.strictEqual(calculateNumber(0, 2.9), 3); // 0 and 2.9 rounds to 3
  });
});
