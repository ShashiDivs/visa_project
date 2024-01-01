from flask import Flask
from visa.logger import logging

app = Flask(__name__)
@app.route("/", methods = ['GET','POST'])
def index():
    logging.info("we are just test logging module")
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)