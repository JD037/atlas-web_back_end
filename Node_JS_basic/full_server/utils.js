import fs from 'fs';
import util from 'util';

const readFile = util.promisify(fs.readFile);

export const readDatabase = async (filePath) => {
  try {
    const data = await readFile(filePath, { encoding: 'utf8' });
    // Process the data as needed for your application
    return data; // Modify this to return an object of arrays as required
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
