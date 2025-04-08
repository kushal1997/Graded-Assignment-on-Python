from flask import Flask
from read_config import config_reader

from pymongo import MongoClient

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["config_db"]
    collection = db["data"]
except Exception as e:
    print(f"error: {e}")

filename = '.config'
config = config_reader(filename)
print("Config data : ", config)
config["filename"] = filename 

d = collection.find_one({"filename" : filename})
if not d:
    collection.insert_one(config)


if __name__ == '__main__':
    app.run(debug = True)