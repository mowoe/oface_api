from flask import Flask
from flask import request
from flask import jsonify
from utils import *
import time
import hashlib
import numpy as np
import json

app = Flask(__name__)
 

@app.route('/detect')
def detect():
    start = time.time()
    image_url = request.args.get('url')
    if validate(image_url):
        results = {}
        hashname = hashlib.sha224(str(time.time())).hexdigest()
        fname = "/tmp/"+hashname + ".jpg"
        download_image(image_url,fname)
        results["detected"] = detect_face(fname)
        results["id"] = hashname
        results["time"] = time.time()-start
        return json.dumps(results)
    else:
        return error_generator("invalid_url")

app.run(host="0.0.0.0")