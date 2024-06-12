from flask import Flask, request, jsonify
from queue import Queue
import threading
import time

app = Flask(__name__)
data_queue = Queue()

@app.route("/")
def index():
    return "Welcome to the URL used as a webhook receiver!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    data_queue.put(data)
    return "Request succeeded", 200

@app.route('/show_json', methods=['GET'])
def show_json():
    time.sleep(20)
    if data_queue.empty():
        return jsonify({"message": "No data available"}), 200
    else:
        data_to_return = data_queue.get()
        return jsonify(data_to_return)

if __name__ == '__main__':
    app.run(port=5000)

