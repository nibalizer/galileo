# nostrild
# authentication daemon

import yaml

from itsdangerous import TimestampSigner
from flask import Flask, abort, request, jsonify
app = Flask(__name__)


def always_auth():
    req = request.get_json(force=True)
    print req
    if req['user'] is None:
        abort(400, "You must specify a user")
    if req['password'] is None:
        abort(400, "You must specify a password")

    secret = s.sign(req['user'])
    return secret



@app.route("/")
def hello():
    return "nostrild: authentication for snot"


@app.route("/auth", methods = ["POST"])
def auth():
    if conf['auth_scheme'] == 'always':
        secret = always_auth()
    elif conf['auth_scheme'] == 'ldap':
        secret = ldap_auth()

    return jsonify({"secret_key": secret,
            "timeout": conf['auth_timeout']})



if __name__ == "__main__":
    with open('config.yaml') as f:
        conf = yaml.load(f.read())
    f.closed
    s = TimestampSigner(conf['secret_key'])

    app.run(debug=True, port=conf['port'])
