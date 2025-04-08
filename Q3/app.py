from flask import Flask, jsonify
from read_config import config_reader
from format_data import format_config_data
from pymongo import MongoClient

app = Flask(__name__)

# setup mongo db connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["config_db"]
    collection = db["data"]
except Exception as e:
    print(f"error: {e}")

# read the config file
filename = '.config'
config = config_reader(filename)

# store filename for better identification
config["filename"] = filename 

# add or update data in MongoDB
d = collection.find_one({"filename" : filename})
if not d:
    collection.insert_one(config)
elif d:
    collection.delete_one({"filename" : filename})
    collection.insert_one(config)


# define API route to fetch data of a single file or all files
@app.route("/fetch/<filename>", methods = ['GET'])
def fetch_details(filename):
    try:

        # returns all file datas
        if filename == 'all':
            d = list(collection.find({},{'_id' : 0}))
            formated = []
            for data in d:
                file_name = data.get("filename","")
                formatted_file_data = [f'filename: {file_name}']
                formatted_file_data += format_config_data(data)
                formated.append(formatted_file_data)

            return jsonify({
                "message" : "data all files fetched successfully",
                "data" : formated
            })
        
        # return specific data as per the file name
        d = collection.find_one({"filename" : filename},{'_id' : 0})
      
        if d:
            return jsonify({
            "message" : "Data successfully fetched",
            "data" :   format_config_data(d)
        })
        else:
            return jsonify({
                "message" : "this file data doesn't exit in database"
            })
    except Exception as e:
        return jsonify({
            "message": f"Internal server error: {e}"
        }),500


# to run flask server
if __name__ == '__main__':
    app.run(debug = True)