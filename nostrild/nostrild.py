# nostrild
# authentication daemon

import yaml

from itsdangerous import TimestampSigner
from flask import Flask, abort, request, jsonify
app = Flask(__name__)



@app.route("/")
def hello():
    return "nostrild: authentication for snot"



if __name__ == "__main__":
    with open('config.yaml') as f:
        conf = yaml.load(f.read())
    f.closed

    app.run(debug=True, port=conf['port'])
