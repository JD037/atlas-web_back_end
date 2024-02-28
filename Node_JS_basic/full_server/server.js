import express from 'express';
import routes from './routes/index.js';

const app = express();
const PORT = 1245;

app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

export default app;
