from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    payload = {
        "message": "Hello world",
    }

    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)