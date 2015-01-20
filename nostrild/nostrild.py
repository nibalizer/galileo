# nostrild
# authentication and user info daemon

import getent
import os

import yaml
import ldap

from itsdangerous import TimestampSigner
from flask import Flask, abort, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)




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

  con = ldap.initialize("ldap://" + conf['ldap_server'])
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
    print request.json
    if conf['auth_scheme'] == 'always':
        secret = always_auth()
    elif conf['auth_scheme'] == 'ldap':
        secret = ldap_auth()

    return jsonify({"secret_key": secret,
            "timeout": conf['auth_timeout']})


@app.route("/user/<name>")
def username(name):
    """
    return getent info and snotsig
    """
    try:
        passwd = dict(getent.passwd(name))
    except TypeError:
        abort(400, "Invalid user")
    snotsig_path = '/home/{0}/solaris/.snotsig'.format(name)
    sig_path = '/home/{0}/solaris/.snotsig'.format(name)
    if os.path.isfile(snotsig_path):
        with open(snotsig_path) as f:
            snotsig = f.read()
        f.closed
    elif os.path.isfile(sig_path):
        with open(sig_path) as f:
            snotsig = f.read()
        f.closed
    #TODO check linux homedir as well
    else:
        snotsig = ""
    return jsonify({"passwd": passwd, "snotsig": snotsig})


if __name__ == "__main__":
    with open('config.yaml') as f:
        conf = yaml.load(f.read())
    f.closed
    s = TimestampSigner(conf['secret_key'])

    app.run(debug=True, port=conf['port'])
