# Booger D 2
# REST API in front of snot
import subprocess
import pysnot


from flask import Flask, abort, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Boogerd 2"


@app.route("/v1/ticket/<int:ticket_number>")
def ticket_get(ticket_number):

    tic = pysnot.get_ticket(ticket_number)
    return tic


@app.route("/v1/ticket/<int:ticket_number>/raw")
def ticket_get_raw(ticket_number):

    tic = pysnot.get_ticket_raw(ticket_number)
    return tic


@app.route("/v1/ticket/<int:ticket_number>/flags")
def ticket_flags_get(ticket_number):

    flags = pysnot.get_flags(ticket_number)
    return flags


@app.route("/v1/ticket/<int:ticket_number>/reply_to")
def ticket_reply_to_get(ticket_number):

    reply_to_string = pysnot.get_reply_to(ticket_number)
    return reply_to_string


@app.route("/v1/ticket/<int:ticket_number>/subject")
def ticket_subject_get(ticket_number):

    subject = pysnot.get_subject(ticket_number)
    return subject


@app.route("/v1/ticket/<int:ticket_number>/assigned")
def ticket_assigned_get(ticket_number):

    assigned = pysnot.get_assigned(ticket_number)
    return assigned


@app.route("/v1/ticket/<int:ticket_number>/metadata")
def ticket_metadata_get(ticket_number):

    metadata = pysnot.get_metadata(ticket_number)
    return jsonify(metadata)


@app.route("/v1/ticket/<int:ticket_number>/resolve_silent", methods=['POST'])
def ticket_resolve(ticket_number):

    success = pysnot.resolve_ticket_silent(ticket_number)
    return str(success)


@app.route("/v1/all_flags")
def all_flags():

    flags = pysnot.list_all_flags()
    #this looks funky because of
    #http://flask.pocoo.org/docs/0.10/security/#json-security
    return jsonify({"all_flags": flags})


if __name__ == "__main__":
    app.run(debug=True)
