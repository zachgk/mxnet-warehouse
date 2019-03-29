from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId
from bson.json_util import dumps
import json

app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = "mongodb://localhost:27017/mxWarehouse"
CORS(app)

mongo = PyMongo(app)
components = mongo.db.components

@app.route('/')
def index():
    return send_file('static/index.html')

@app.route('/api/components')
def listComponents():
    return dumps({'result': components.find()})

@app.route('/api/components/<component>')
def getComponent(component):
    return dumps({'result': components.find_one({'_id': ObjectId(component)})})

@app.route('/img/<filename>')
# Fix the problem of finding images
def get_image(filename=None):
    return send_file('static/img/'+filename, mimetype='image/png')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #app.debug = True
    app.threaded = True
    app.run()
