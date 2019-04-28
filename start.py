import pyzbar.pyzbar as pyzbar
import base64
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    data = request.get_json()
    image = data['image']
    imgData = base64.b64decode(image)
    decodedObjects = pyzbar.decode(imgData)
    barcode = 'Not recognized'
    for object in decodedObjects:
        barcode = object.data.decode('utf-8')
    return barcode


if __name__ == '__main__':
    app.run(host="159.65.201.192:5000")