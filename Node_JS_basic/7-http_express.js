const express = require('express');
const fs = require('fs').promises;
const app = express();

const databasePath = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const data = await fs.readFile(databasePath, 'utf8');
    const lines = data.split('\n').filter((line) => line);
    // Remove header
    lines.shift();
    const students = lines.map((line) => {
      const [firstname, , , field] = line.split(',');
      return { firstname, field };
    });

    const csStudents = students.filter((student) => student.field === 'CS').map((student) => student.firstname);
    const sweStudents = students.filter((student) => student.field === 'SWE').map((student) => student.firstname);

    res.send(`This is the list of our students\nNumber of students: ${students.length}\nNumber of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\nNumber of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
  } catch (err) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
