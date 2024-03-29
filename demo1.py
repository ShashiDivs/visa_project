from flask import Flask
from visa.logger import logging
from visa.exception import CustomException
import sys,os

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing Custom Exception")
    except Exception as e:
        visa = CustomException(e,sys)
        logging.info(visa.error_message)
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True)