// 9-api/api.test.js
const expect = require('chai').expect;
const request = require('request');

describe('API', function() {
  // Existing tests for the index page...

  describe('GET /cart/:id', function() {
    it('returns Payment methods for a valid numeric id', function(done) {
      request('http://localhost:7865/cart/12', function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });

    it('returns 404 for an invalid id', function(done) {
      request('http://localhost:7865/cart/hello', function(error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
