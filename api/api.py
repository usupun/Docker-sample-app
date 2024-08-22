from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api_endpoint')
def api():
    data = {'message': 'Hello from the API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)