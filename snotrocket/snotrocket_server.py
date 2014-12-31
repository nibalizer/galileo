
from flask import Flask, jsonify

import pysnotrocket

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tickets/number/<int:number>")
def get_ticket_number(number):
    resp = pysnotrocket.get_ticket_by_number(number)
    return jsonify(resp)


@app.route("/tickets/uuid/<uuid>")
def get_ticket_uuid(uuid):
    resp = pysnotrocket.get_ticket_by_uuid(uuid)
    return jsonify(resp)


@app.route("/tickets/open")
def find_open_tickets_bare():
    num_resp, tickets= pysnotrocket.get_open_tickets()
    return jsonify({"total": num_resp, "tickets": tickets})


@app.route("/ticket/open/from=<int:index_from>/size=<int:size>")
def find_open_tickets(index_from, size):
    num_resp, tickets = pysnotrocket.get_open_tickets(index_from, size)
    return jsonify({"total": num_resp, "tickets": tickets})


if __name__ == "__main__":
    app.run(debug=True,port=5001)
