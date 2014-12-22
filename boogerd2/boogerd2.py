

# Booger D 2
# REST API in front of snot
import subprocess



from flask import Flask, abort, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/ticket/get/<ticket_number>")
def ticket_get(ticket_number):

    subproc = subprocess.Popen(['testsnot', '-s', ticket_number], stdout=subprocess.PIPE)
    tic = subproc.communicate()

    return tic

if __name__ == "__main__":
    app.run(debug=True)
