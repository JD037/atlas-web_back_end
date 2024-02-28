// 3-main_1.js
const countStudents = require('./3-read_file_async');

countStudents("database.csv")
  .then(() => {
    console.log("Done!");
  })
  .catch((error) => {
    console.log(error.message);
  });

console.log("After!");
