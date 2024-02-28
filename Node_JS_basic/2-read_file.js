// 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    // Read the file synchronously
    data = fs.readFileSync(path, { encoding: 'utf8' });
  } catch (error) {
    // If the file cannot be read, throw an error
    throw new Error('Cannot load the database');
  }

  // Split the data into lines
  const lines = data.split('\n').filter((line) => line !== '');

  // Remove the header row
  lines.shift();

  // Process the data
  const students = lines.map((line) => line.split(','));

  console.log(`Number of students: ${students.length}`);

  // Count students by field
  const fields = {};
  students.forEach((student) => {
    const field = student[3];
    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(student[0]);
  });

  Object.keys(fields).forEach((field) => {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  });
}

module.exports = countStudents;
