

# Booger D 2
# REST API in front of snot
import subprocess



from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/v1/ticket/get")
def ticket_get():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
