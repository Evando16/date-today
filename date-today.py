import datetime
from flask import Flask, request
import os
import json

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Date today!", 200

@app.route('/today', methods=['GET'])
def today():
    i = datetime.datetime.now()

    result = {'date': "%s/%s/%s" % (i.day, i.month, i.year)}
    return json.dumps(result), 200

port=os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))