// 4-payment.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi with stub', function() {
  let consoleSpy;

  beforeEach(function() {
    // Stub the calculateNumber function to always return 10
    sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console.log to verify it gets called with the correct message
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    // Restore the original functionality after each test
    Utils.calculateNumber.restore();
    console.log.restore();
  });

  it('correctly calls the stubbed calculateNumber and logs the correct total', function() {
    sendPaymentRequestToApi(100, 20);

    // Verify that the stub was called with the expected arguments
    expect(Utils.calculateNumber.calledWith('SUM', 100, 20)).to.be.true;
    // Verify that console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
  });
});
