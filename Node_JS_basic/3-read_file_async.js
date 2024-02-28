// 3-read_file_async.js
const fs = require('fs').promises;

const countStudents = async (path) => {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.split('\n');
    // Remove empty lines and the header
    const students = lines.filter((line) => line && line !== 'firstname,lastname,age,field');

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const [,, , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(student.split(',')[0]);
    });

    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
