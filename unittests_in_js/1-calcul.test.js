// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('sums two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', () => {
    it('subtracts two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('DIVIDE', () => {
    it('divides two rounded numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('returns Error when dividing by zero', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });

  // Additional tests to cover edge cases
  describe('Edge Cases', () => {
    it('handles rounding up correctly', () => {
      assert.strictEqual(calculateNumber('SUM', 1.5, 2.5), 5);
    });

    it('handles negative numbers correctly', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -2.5), 1);
    });

    it('throws an error for invalid type', () => {
      assert.throws(() => calculateNumber('INVALID', 1.4, 4.5), {
        name: 'Error',
        message: 'Invalid type',
      });
    });
  });
});
