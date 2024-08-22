from flask import Flask, request
import requests

app = Flask(__name__)
api_url = "http://myapi_container:8000"  # Assuming the API is running in a container named 'myapi_container' on port 8000

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/call_api')
def fetch_data():
    response = requests.get(f"{api_url}/api_endpoint")
    if response.status_code == 200:
        return response.json()
    else:
        return {'message': 'Failed to fetch data from the API'}

if __name__ == '__main__':
    data = fetch_data()
    app.run(host='0.0.0.0', port=5000)
    # print(data)