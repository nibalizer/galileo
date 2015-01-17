# nostrild
# authentication daemon

import yaml

from itsdangerous import TimestampSigner
from flask import Flask, abort, request, jsonify
app = Flask(__name__)



@app.route("/")
def hello():
    return "nostrild: authentication for snot"


@app.route("/auth", methods = ["POST"])
def auth():
    req = request.get_json(force=True)
    print req
    if req['user'] is None:
        abort(400, "You must specify a user")
    if req['password'] is None:
        abort(400, "You must specify a password")


    return 'yes'



if __name__ == "__main__":
    with open('config.yaml') as f:
        conf = yaml.load(f.read())
    f.closed
    s = TimestampSigner(conf['secret_key'])

    app.run(debug=True, port=conf['port'])
