from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    app.run(debug=True)
