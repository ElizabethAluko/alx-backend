import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to create and store a hash
function createHash() {
    const hashKey = 'HolbertonSchools';
    const hashData = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    client.hset(hashKey, hashData, (err, reply) => {
        if (err) {
            console.error(`Error creating hash: ${err}`);
        } else {
            console.log('Hash created in Redis:');
            redis.print(reply);
        }
    });
}

// Function to display the hash
function displayHash() {
    const hashKey = 'HolbertonSchools';

    client.hgetall(hashKey, (err, reply) => {
        if (err) {
            console.error(`Error getting hash: ${err}`);
        } else {
            console.log('Hash retrieved from Redis:');
            console.log(reply);
        }
    });
}

// Call the functions to create and display the hash
createHash();
displayHash();
