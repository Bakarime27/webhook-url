from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the url used as webhook receiver!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received data: {data}")
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
