// 5-http.js
const http = require('http');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n');
    // Remove the header and empty lines
    const students = lines.slice(1).filter((line) => line.length > 0);

    let csCount = 0;
    let sweCount = 0;
    const csStudents = [];
    const sweStudents = [];

    students.forEach((student) => {
      const [, , , field] = student.split(',');
      if (field === 'CS') {
        csCount += 1;
        csStudents.push(student.split(',')[0]);
      } else if (field === 'SWE') {
        sweCount += 1;
        sweStudents.push(student.split(',')[0]);
      }
    });

    return `Number of students: ${students.length}\n`
           + `Number of students in CS: ${csCount}. List: ${csStudents.join(', ')}\n`
           + `Number of students in SWE: ${sweCount}. List: ${sweStudents.join(', ')}`;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const data = await countStudents(process.argv[2]);
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(`This is the list of our students\n${data}`);
    } catch (error) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Cannot load the database');
    }
  }
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

module.exports = app;
