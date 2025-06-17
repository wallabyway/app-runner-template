from flask import Flask, request, jsonify, send_file
from utils import get_token, upload_file, translate, status, list_bucket
app = Flask(__name__)
@app.route('/')
def index():
    return send_file('viewer.html')
@app.route('/api/token')
def api_token():
    return jsonify({"access_token": get_token()})
@app.route('/api/upload', methods=['POST'])
def api_upload():
    token = get_token()
    f = request.files['file']
    urn = upload_file(token, f.filename, f.read())
    urn_b64 = translate(token, urn)
    return jsonify({"urn": urn_b64})
@app.route('/api/status/<urn>')
def api_status(urn):
    token = get_token()
    return jsonify(status(token, urn))
@app.route('/api/list')
def api_list():
    token = get_token()
    return jsonify(list_bucket(token))
if __name__ == '__main__':
    app.run(port=8080) 
