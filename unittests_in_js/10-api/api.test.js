// 10-api/api.test.js
const request = require('request');
const { expect } = require('chai');

// Describing the test suite for the index page
describe('Index and Cart Endpoints', function() {
    // Test for the index page
    describe('Index page', function() {
        it('should return 200 OK with a welcome message', function(done) {
            request.get('http://localhost:7865', function(error, response, body) {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });

    // Tests for the cart page
    describe('Cart page', function() {
        it('should return 200 and the correct message for a numeric ID', function(done) {
            request.get('http://localhost:7865/cart/12', function(error, response, body) {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Payment methods for cart 12');
                done();
            });
        });

        it('should return 404 for a non-numeric ID', function(done) {
            request.get('http://localhost:7865/cart/hello', function(error, response, body) {
                expect(response.statusCode).to.equal(404);
                done();
            });
        });
    });
});

// Describing the test suite for available payments and login functionality
describe('Available Payments and Login Endpoints', function() {
    // Test for available payment methods
    describe('Available payment methods', function() {
        it('should return 200 with payment methods object', function(done) {
            request.get('http://localhost:7865/available_payments', function(error, response, body) {
                expect(response.statusCode).to.equal(200);
                expect(JSON.parse(body)).to.deep.equal({
                    payment_methods: {
                        credit_cards: true,
                        paypal: false
                    }
                });
                done();
            });
        });
    });

    // Test for login functionality
    describe('Login functionality', function() {
        it('should welcome a user when username is provided', function(done) {
            const options = {
                url: 'http://localhost:7865/login',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ userName: 'Betty' })
            };

            request(options, function(error, response, body) {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome Betty');
                done();
            });
        });
    });
});
