
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from itsdangerous import TimestampSigner

import pysnotrocket


app = Flask(__name__)
cors = CORS(app)



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/tickets/number/<int:number>")
def get_ticket_number(number):
    print request.headers
    try:
        s.unsign(request.headers['X-SNOT-Auth-Key'], max_age=1500)
    except:
        abort(401)
    resp = pysnotrocket.get_ticket_by_number(number)
    content = pysnotrocket.get_ticket_content(number)
    resp['content'] = content
    return jsonify(resp)


@app.route("/v1/tickets/uuid/<uuid>")
def get_ticket_uuid(uuid):
    resp = pysnotrocket.get_ticket_by_uuid(uuid)
    content = pysnotrocket.get_ticket_content(resp['number'])
    resp['content'] = content
    return jsonify(resp)


@app.route("/v1/tickets/open")
def find_open_tickets_bare():
    num_resp, tickets= pysnotrocket.get_open_tickets()
    return jsonify({"total": num_resp, "tickets": tickets})


@app.route("/v1/ticket/open/from=<int:index_from>/size=<int:size>")
def find_open_tickets(index_from, size):
    num_resp, tickets = pysnotrocket.get_open_tickets(index_from, size)
    return jsonify({"total": num_resp, "tickets": tickets})


if __name__ == "__main__":
    s = TimestampSigner('secretstring')
    app.run(debug=True,port=5001)
