// Import necessary modules
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Create a Kue queue
const queue = kue.createQueue();

const app = express();
const port = 1245;

// Set the initial number of available seats
client.set('available_seats', 50);

// Initialize the reservationEnabled flag
let reservationEnabled = true;

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getAsync('available_seats');
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create and queue a job
  const job = queue.create('reserve_seat', {}).save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    try {
      const availableSeats = await getAsync('available_seats');
      if (availableSeats === '0') {
        reservationEnabled = false;
        done(new Error('Not enough seats available'));
      } else {
        // Decrease the number of available seats and save it in Redis
        const newAvailableSeats = parseInt(availableSeats) - 1;
        client.set('available_seats', newAvailableSeats);
        if (newAvailableSeats === 0) {
          reservationEnabled = false;
        }
        done();
      }
    } catch (error) {
      done(error);
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
