// 2-calcul_chai.test.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber with Chai', () => {
  describe('SUM', () => {
    it('sums two rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', () => {
    it('subtracts two rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('DIVIDE', () => {
    it('divides two rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('returns Error when dividing by zero', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });

  // Additional tests to cover edge cases
  describe('Edge Cases with Chai', () => {
    it('handles rounding up correctly', () => {
      expect(calculateNumber('SUM', 1.5, 2.5)).to.equal(5);
    });

    it('handles negative numbers correctly', () => {
      expect(calculateNumber('SUBTRACT', -1.4, -2.5)).to.equal(1);
    });

    it('throws an error for invalid type', () => {
      expect(() => calculateNumber('INVALID', 1.4, 4.5)).to.throw('Invalid type');
    });
  });
});
