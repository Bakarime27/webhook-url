from flask import Flask, request, jsonify
from queue import Queue
import time
import threading

app = Flask(__name__)
data_queue = Queue()
data_event = threading.Event()

@app.route("/")
def index():
    return "Welcome to the URL used as a webhook receiver!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and isinstance(data, dict) and data:  # Check if data is not empty and is a dictionary
        data_queue.put(data)
        data_event.set()  # Signal that data is available
        return "Request succeeded", 200
    else:
        return jsonify({"message": "No data received or data is empty"}), 400

@app.route('/show_json', methods=['GET'])
def show_json():
    if not data_event.is_set():
        # Wait for data to become available
        data_event.wait(timeout=25)  # Timeout after 25 seconds to avoid infinite wait
    
    if data_queue.empty():
        return jsonify({"message": "No data available"}), 200
    else:
        data_to_return = data_queue.get()
        data_event.clear()  # Reset the event after getting the data
        return jsonify(data_to_return)

if __name__ == '__main__':
    app.run(port=5000)

