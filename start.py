import pyzbar.pyzbar as pyzbar
import base64
import cv2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    data = request.get_json()
    image = data['image']
    imgData = base64.b64decode(image)
    fileName = 'sample.jpg'
    with open('sample.jpg', 'wb') as f:
        f.write(imgData)
    img = cv2.imread(fileName)
    decodedObjects = pyzbar.decode(img)
    barcode = 'Not recognized'
    for object in decodedObjects:
        barcode = object.data.decode('utf-8')
    return barcode


if __name__ == '__main__':
    app.run(host='0.0.0.0')