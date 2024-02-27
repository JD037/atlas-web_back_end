// Task 0 - Contains test cases of this function
// assume a and b are numbers
// tests should be around the "rounded" part

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return the sum of rounded a and b', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the sum when one is rounded up and the other is rounded down', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the sum when both are rounded up', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should handle rounding up to the next integer correctly', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  
  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1, -2), -3);
    assert.strictEqual(calculateNumber(-1.4, 2.6), 2);
  });

  // it('should round half up according to Math.round standard', function() {
  //   assert.strictEqual(calculateNumber(1.5, 2.5), 5);
  //   assert.strictEqual(calculateNumber(-0.5, 0.5), 0);
  // });

  it('should return the sum when both numbers are decimals', function() {
    assert.strictEqual(calculateNumber(0.1, 0.2), 0); // Due to rounding, 0.1+0.2 is expected to be 0
    assert.strictEqual(calculateNumber(0.9, 1.1), 2); // 0.9 rounds to 1, 1.1 rounds to 1
  });

  // it('should handle large numbers correctly', function() {
  //   assert.strictEqual(calculateNumber(1000.4, 2000.5), 3001);
  //   assert.strictEqual(calculateNumber(-1000.5, 1000.5), 0);
  // });

  it('should return the first number when the second one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(1.2, 0.49), 1);
  });

  it('should return the second number when the first one is 0 after rounding', function() {
    assert.strictEqual(calculateNumber(0.49, 2.5), 3);
  });

  it('should handle zero correctly', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(0, 2.9), 3);
  });
});
