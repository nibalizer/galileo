# Booger D 2
# REST API in front of snot
import subprocess
import pysnot


from flask import Flask, abort, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/ticket/<ticket_number>")
def ticket_get(ticket_number):

    tic = pysnot.get_ticket(ticket_number)
    return tic


@app.route("/v1/ticket/<ticket_number>/flags")
def ticket_flags_get(ticket_number):

    flags = pysnot.get_flags(ticket_number)
    return flags


@app.route("/v1/ticket/<ticket_number>/assigned")
def ticket_assigned_get(ticket_number):

    assigned = pysnot.get_assigned(ticket_number)
    return assigned


@app.route("/v1/ticket/<ticket_number>/metadata")
def ticket_metadata_get(ticket_number):

    metadata = pysnot.get_metadata(ticket_number)
    return jsonify(metadata)


@app.route("/v1/all_flags")
def all_flags():

    flags = pysnot.list_all_flags()
    #this looks funky because of
    #http://flask.pocoo.org/docs/0.10/security/#json-security
    return jsonify({"all_flags": flags})


if __name__ == "__main__":
    app.run(debug=True)
