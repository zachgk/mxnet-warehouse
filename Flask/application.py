from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import json

application = Flask(__name__)
CORS(application)


@application.route('/')
def index():
    return "Hello World"

@application.route('/search',methods=['POST'])
def search():
    data = request.get_json()
    if data["keyword"]:
        to_return = {"result": [{"name": "resnet-50", "type": "symbol-params", "symbol_url": "https://sample.com/res50-symbol.json", "params_url": "https://sample.com/res50-0000.param"}]}
    return jsonify(**to_return)

@application.route('/img/<filename>')
# Fix the problem of finding images
def get_image(filename=None):
    return send_file('static/img/'+filename, mimetype='image/png')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.threaded = True
    application.run()