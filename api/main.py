import re
from fastapi import FastAPI
from pymongo import MongoClient

# MongoDB connection details
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
MONGO_DB = 'whoshittin'
MONGO_COLLECTION = 'venue'
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'example'
mongdb_uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"
mongo_client = MongoClient(mongdb_uri)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

app = FastAPI()

@app.get("/")
def venue():

    return {"detail": "found"}

@app.get("/venue/{venue_name}")
def venue(venue_name: str):

    return {venue_name: "world"}
