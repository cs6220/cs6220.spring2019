"""
To run this app, in your terminal:
> export FLASK_ENV=development
> export FLASK_APP=flask_demo.py
> flask run

Navigate to:
> http://127.0.0.1:5000/
> http://127.0.0.1:5000/predict/5
> http://127.0.0.1:5000/predict/11
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/predict/<int:number>')
def predict(number):
    if number < 10:
        return "I predict " + str(number) + " is less than 10!"
    else:
    	# NOTE: An input greater than 10 will generate an error.
        # Use the information in the traceback to fix the problem.
        return "I predict " + number + " is greater than or equal to 10!"
