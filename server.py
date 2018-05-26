from flask import Flask
from flask import request
from flask import jsonify
from utils import *
app = Flask(__name__)
 

@app.route('/detect')
def detect():
    image_url = request.args.get('url')
    if validate(image_url):
        results = {}
        download_image(image_url,"/tmp/img.jpg")
        results["detected"] = detect_face("/tmp/img.jpg")
        return jsonify(str(results))
    else:
        return error_generator("url")

app.run(host="0.0.0.0")