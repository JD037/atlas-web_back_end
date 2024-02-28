// 10-api/api.js
const express = require('express');
// Initialize the express application
const app = express();

// Middleware to parse JSON bodies of incoming requests
app.use(express.json());

// Route for the index page
// GET request to root ('/') returns a welcome message
app.get('/', (req, res) => {
    // Send a 200 OK status code and a welcome message
    res.status(200).send('Welcome to the payment system');
});

// Route for retrieving payment methods for a specific cart
// GET request to '/cart/:id', where :id must be a number
app.get('/cart/:id(\\d+)', (req, res) => {
    // Extract the cart ID from the request parameters
    const idToSend = req.params.id;
    // Send a 200 OK status code and the payment methods message
    res.status(200).send(`Payment methods for cart ${idToSend}`);
});

// Route for available payment methods
// GET request to '/available_payments' returns available payment methods
app.get('/available_payments', (req, res) => {
    // Respond with a JSON object detailing available payment methods
    res.status(200).json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

// Route for user login
// POST request to '/login' to log in a user
app.post('/login', (req, res) => {
    // Extract the userName from the request body
    const userName = req.body.userName;
    // Send a 200 OK status code and a welcome message to the user
    res.status(200).send(`Welcome ${userName}`);
});

// Start the server and listen on port 7865
app.listen(7865, () => {
    console.log('API available on localhost port 7865');
});

// Export the app for testing purposes
module.exports = app;
