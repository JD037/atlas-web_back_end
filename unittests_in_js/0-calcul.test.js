// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  // Test for both numbers rounded
  describe('both numbers rounded', () => {
    it('correctly calculates the sum of 1.5 and 3.7 as 6', () => {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  // Test for first number rounded
  describe('first number rounded', () => {
    it('correctly calculates the sum of 1.5 and 3 as 5', () => {
      assert.strictEqual(calculateNumber(1.5, 3), 5);
    });
  });

  // Test for second number rounded
  describe('second number rounded', () => {
    it('correctly calculates the sum of 1 and 3.7 as 5', () => {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  // Additional tests to cover edge cases and ensure comprehensive testing
  // Edge case: both numbers just below .5 threshold
  it('rounds both numbers down when below .5 threshold', () => {
    assert.strictEqual(calculateNumber(1.4, 2.4), 3);
  });

  // Edge case: one number rounded up, one rounded down
  it('rounds one number up and one number down correctly', () => {
    assert.strictEqual(calculateNumber(1.5, 2.4), 4);
  });

  // Edge case: both numbers just above .5 threshold
  it('rounds both numbers up when above .5 threshold', () => {
    assert.strictEqual(calculateNumber(1.6, 2.5), 5);
  });
});
