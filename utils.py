from flask import jsonify
import urllib
import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def validate(url):
    if not "://" in url:
        return 0 
    return 1


def error_generator(err):
    if "url" in err:
        return jsonify("{'status': 'error','reason': 'invalid_url'}")

def detect_face(fname):
    out = {}
    image = cv2.imread(fname)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print "Found {0} faces!".format(len(faces))
    for x in range(len(faces)):
        out[x] = tuple(faces[x])
    return out

def download_image(url,fname):
    urllib.urlretrieve(url,fname)