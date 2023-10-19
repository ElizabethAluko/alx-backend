import express from 'express';
import redis from 'redis';
import kue from 'kue';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by ID
const getItemById = (id) => {
  return listProducts.find((product) => product.itemId === id);
};

// Function to reserve stock by item ID
const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

// Async function to get the currently reserved stock by item ID
const getCurrentReservedStockById = async (itemId) => {
  return new Promise((resolve, reject) => {
    client.get(`item.${itemId}`, (err, reply) => {
      if (err) reject(err);
      else resolve(Number(reply));
    });
  });
};

// Middleware to handle JSON responses
app.use(express.json());

// Route to list all products
app.get('/list_products', (req, res) => {
  const productsWithStock = listProducts.map((product) => {
    return {
      ...product,
      currentQuantity: product.initialAvailableQuantity - getCurrentReservedStockById(product.itemId),
    };
  });
  res.json(productsWithStock);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = product.initialAvailableQuantity - (await getCurrentReservedStockById(itemId));
  res.json({ ...product, currentQuantity });
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = product.initialAvailableQuantity - (await getCurrentReservedStockById(itemId));

  if (currentQuantity <= 0) {
    return res.status(400).json({ status: 'Product out of stock' });
  }

  // Reserve one unit of the product
  const currentReservedStock = await getCurrentReservedStockById(itemId);
  reserveStockById(itemId, currentReservedStock + 1);

  res.json({ status: 'Reservation confirmed' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
