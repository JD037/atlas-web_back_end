// 1-redis_op.js

import redis from 'redis';
const client = redis.createClient();

client.on('ready', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`)
});

client.on('ready', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`)
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
      console.log(reply);
  });
}

// Using functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');