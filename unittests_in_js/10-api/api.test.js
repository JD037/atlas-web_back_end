// 10-api/api.test.js
const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = chai;
const server = require('./api');

chai.use(chaiHttp);

describe('API', function() {
  // Existing tests...

  describe('GET /available_payments', function() {
    it('returns the correct payment methods', function(done) {
      chai.request(server)
        .get('/available_payments')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.body).to.deep.equal({
            payment_methods: {
              credit_cards: true,
              paypal: false
            }
          });
          done();
        });
    });
  });

  describe('POST /login', function() {
    it('welcomes the user by username', function(done) {
      chai.request(server)
        .post('/login')
        .send({ userName: 'Betty' })
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.text).to.equal('Welcome Betty');
          done();
        });
    });
  });
});
