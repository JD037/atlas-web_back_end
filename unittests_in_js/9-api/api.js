// 9-api/api.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Adding new endpoint with regex validation for numeric ID
app.get('/cart/:id(\\d+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app; // Export for testing
