// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  // Testing the rounding of the first argument
  describe('rounding the first argument', function() {
    it('rounds the first argument down when less than .5', function() {
      assert.strictEqual(calculateNumber(1.3, 0), 1);
    });

    it('rounds the first argument up when .5 or more', function() {
      assert.strictEqual(calculateNumber(1.7, 0), 2);
    });

    it('handles the first argument when an integer', function() {
      assert.strictEqual(calculateNumber(1.0, 0), 1);
    });
  });

  // Testing the rounding of the second argument
  describe('rounding the second argument', function() {
    it('rounds the second argument down when less than .5', function() {
      assert.strictEqual(calculateNumber(0, 1.3), 1);
    });

    it('rounds the second argument up when .5 or more', function() {
      assert.strictEqual(calculateNumber(0, 1.7), 2);
    });

    it('handles the second argument when an integer', function() {
      assert.strictEqual(calculateNumber(0, 1.0), 1);
    });
  });

  // Testing the correct sum of rounded arguments
  describe('correct sum of rounded arguments', function() {
    it('correctly calculates the sum of two rounded numbers', function() {
      assert.strictEqual(calculateNumber(1.3, 1.3), 2);
      assert.strictEqual(calculateNumber(1.7, 1.2), 3);
      assert.strictEqual(calculateNumber(1.3, 1.8), 3);
      assert.strictEqual(calculateNumber(1.6, 1.8), 4);
    });

    it('handles when one argument rounds to 0', function() {
      assert.strictEqual(calculateNumber(1.3, 0), 1);
      assert.strictEqual(calculateNumber(0, 1.2), 1);
    });
  });
});
