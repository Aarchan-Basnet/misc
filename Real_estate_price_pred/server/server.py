from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi"


if __name__ == "main":
    print("Starting python flask server for Home Price Prediction....")
    app.run()
