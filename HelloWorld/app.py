from flask import Flask
from metainfo import SERVICE_NAME, VERSION
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/metainfo")
def metainfo():
    return f"<h1 style='color:blue'>ServiceName: {SERVICE_NAME} Version: {VERSION}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')




