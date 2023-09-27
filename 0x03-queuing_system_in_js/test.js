import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis Client Error', err))
  .connect();

await client.set('key2', 'Jesus is Lord');
const value = await client.get('key2');
await client.disconnect();
