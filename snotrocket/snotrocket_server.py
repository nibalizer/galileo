
import yaml
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from itsdangerous import TimestampSigner

import pysnotrocket


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'X-SNOT-Auth-Key'
cors = CORS(app)

def verify_auth():
    if conf['verify_auth']:
        try:
            s.unsign(request.headers['X-SNOT-Auth-Key'], max_age=1500)
        except:
            abort(401)


@app.route("/")
def hello():
    return "SnotRocket: search and read for SNOT"


@app.route("/v1/tickets/number/<int:number>")
def get_ticket_number(number):
    verify_auth()
    resp = pysnotrocket.get_ticket_by_number(number)
    content = pysnotrocket.get_ticket_content(number)
    resp['content'] = content
    return jsonify(resp)


@app.route("/v1/tickets/uuid/<uuid>")
def get_ticket_uuid(uuid):
    verify_auth()
    resp = pysnotrocket.get_ticket_by_uuid(uuid)
    content = pysnotrocket.get_ticket_content(resp['number'])
    resp['content'] = content
    return jsonify(resp)


@app.route("/v1/tickets/open")
def find_open_tickets_bare():
    verify_auth()
    num_resp, tickets= pysnotrocket.get_open_tickets()
    return jsonify({"total": num_resp, "tickets": tickets})


@app.route("/v1/ticket/open/from=<int:index_from>/size=<int:size>")
def find_open_tickets(index_from, size):
    verify_auth()
    num_resp, tickets = pysnotrocket.get_open_tickets(index_from, size)
    return jsonify({"total": num_resp, "tickets": tickets})


if __name__ == "__main__":
    with open('config.yaml') as f:
        conf = yaml.load(f.read())
    f.closed
    s = TimestampSigner(conf['secret_key'])

    app.run(debug=conf['debug'],port=conf['port'])
