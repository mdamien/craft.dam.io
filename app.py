import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def get_map():
    if request.method == 'POST':
        map = json.loads(request.form['data'])
        open('map.json', 'w').write(json.dumps(map))
    return jsonify(json.load(open('map.json')))