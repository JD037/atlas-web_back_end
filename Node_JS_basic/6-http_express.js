// Import express
const express = require('express');

// Create an instance of express
const app = express();

// Define a route for the root path ('/') to send a response
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the app listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for testing or for further use
module.exports = app;
