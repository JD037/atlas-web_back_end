// api.test.js
const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = chai;
const server = require('./api');

chai.use(chaiHttp);

describe('Index page', () => {
  it('returns the correct status code', (done) => {
    chai.request(server)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('returns the correct result', (done) => {
    chai.request(server)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
