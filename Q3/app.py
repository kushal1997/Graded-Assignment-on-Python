from flask import Flask, jsonify
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
elif d:
    collection.update_one({"filename" : filename},{'$set' : config})


@app.route("/fetch/<filename>", methods = ['GET'])
def fetch_details(filename):
    try:
        if filename == 'all':
            d = list(collection.find({},{'_id' : 0}))
            return jsonify({
                "message" : "data all files fetched successfully",
                "data" : d
            })
        d = collection.find_one({"filename" : filename},{'_id' : 0})
        if d:
            return jsonify({
            "message" : "Data successfully fetched",
            "data" : d
        })
        else:
            return jsonify({
                "message" : "this file data doesn't exit in database"
            })
    except Exception as e:
        return jsonify({
            "message": f"Internal server error: {e}"
        }),500


if __name__ == '__main__':
    app.run(debug = True)