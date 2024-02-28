// 10-api/api.js
const express = require('express');
const app = express();
app.use(express.json()); // Middleware to parse JSON bodies

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// New endpoint for GET /available_payments
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// New endpoint for POST /login
app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

const PORT = 7865;
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app; // Export for testing
