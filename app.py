from flask import Flask, request, jsonify
import json

app = Flask(__name__)
received_data = {}

@app.route("/")
def index():
    return "Welcome to the url used as webhook receiver!"

@app.route('/webhook', methods=['POST'])
def webhook():
    global received_data
    data = request.json
    received_data = data
    print(f"Received data: {data}")
    return '', 200

@app.route('/show_json', methods=['GET'])
def show_json():
    global received_data
    # Copy the current data to return it
    data_to_return = received_data.copy()
    # Clear the received_data dictionary
    received_data.clear()
    return jsonify(data_to_return)

if __name__ == '__main__':
    app.run(port=5000)
