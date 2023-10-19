import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting ${schoolName} in Redis: ${err}`);
        } else {
            console.log(`Set ${schoolName} in Redis with value: ${value}`);
            redis.print(reply);
        }
    });
}

// Function to display the value of a school in Redis
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error getting ${schoolName} from Redis: ${err}`);
        } else {
            console.log(`Value of ${schoolName} in Redis: ${reply}`);
        }
    });
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
