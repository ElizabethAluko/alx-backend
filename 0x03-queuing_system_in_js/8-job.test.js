const kue = require('kue');
const chai = require('chai');
const { createPushNotificationsJobs } = require('./8-job');
const queue = kue.createQueue();

chai.should();
const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  before((done) => {
    kue.app.listen(3000);
    done();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid', queue)).to.throw('Jobs is not an array');
  });

  it('should add jobs to the queue and validate their presence', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs.length.should.equal(2);

    const job1 = queue.testMode.jobs[0];
    const job2 = queue.testMode.jobs[1];

    job1.type.should.equal('push_notification_code_3');
    job2.type.should.equal('push_notification_code_3');

    done();
  });

  after((done) => {
    queue.testMode.clear();
    done();
  });
});
