import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase('path/to/database.csv');
      // Process and format the data as required
      res.status(200).send('Formatted student data');
    } catch (error) {
      res.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase('path/to/database.csv');
      // Filter and format the data based on major
      res.status(200).send('Filtered student data by major');
    } catch (error) {
      res.status(500).send(error.message);
    }
  }
}

export default StudentsController;
