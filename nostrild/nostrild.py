# nostrild
# authentication daemon

from flask import Flask, abort, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "nostrild: authentication for snot"



if __name__ == "__main__":
    app.run(debug=True)
