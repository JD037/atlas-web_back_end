// 6-payment_token.test.js
const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('returns a resolved promise with the correct data on success', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // Indicate that the test is complete
      })
      .catch((error) => {
        done(error); // Pass any errors to done to fail the test
      });
  });
});
