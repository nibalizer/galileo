# nostrild
# authentication daemon

import ldap

import yaml

from itsdangerous import TimestampSigner
from flask import Flask, abort, request, jsonify
app = Flask(__name__)


def always_auth():
    req = request.get_json(force=True)
    if req['user'] is None:
        abort(400, "You must specify a user")
    if req['password'] is None:
        abort(400, "You must specify a password")

    secret = s.sign(req['user'])
    return secret


def ldap_auth():

  req = request.get_json(force=True)
  if req['user'] is None:
      abort(400, "You must specify a user")
  if req['password'] is None:
      abort(400, "You must specify a password")

  con = ldap.initialize("ldap://openldap.cat.pdx.edu")
  con.start_tls_s()

  try:
    dn = "uid={0},{1}".format(req['user'], conf['search_scope'])
    pw = "{0}".format(req['password'])
    con.simple_bind_s( dn, pw )
    success = True

  except:
    success = False

  finally:
    con.unbind()

  if success:
    secret = s.sign(req['user'])
    return secret
  else:
    abort(400, "Invalid username or password")


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
