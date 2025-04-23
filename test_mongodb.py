
from pymongo.mongo_client import MongoClient

MONGO_DB_URL="mongodb+srv://gauravsarthak00:PUBHDSREo5o9wTkC@cluster0.bemyycd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(MONGO_DB_URL)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)