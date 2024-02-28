import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
