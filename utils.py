from flask import jsonify
import urllib
import cv2
import dlib
from skimage import io
import json

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
detector = dlib.get_frontal_face_detector()

def validate(url):
    if not "://" in url:
        return 0 
    return 1


def error_generator(err):
    return jsonify("{'status': 'fail','reason': '"+err+"'}")

def detect_face(fname):
    out = {}
    img = io.imread(fname)
    dets, scores, idx = detector.run(img, 1)
    for i, d in enumerate(dets):
        sq = (d.bottom(),d.right(),d.left(),d.top())
        sq = tuple([int(v) for v in sq])
        out[i] = sq
    return out

def download_image(url,fname):
    urllib.urlretrieve(url,fname)

def getRep(imgPath):
    if args.verbose:
        print("Processing {}.".format(imgPath))
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if args.verbose:
        print("  + Original size: {}".format(rgbImg.shape))

    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    if args.verbose:
        print("  + Face detection took {} seconds.".format(time.time() - start))

    start = time.time()
    alignedFace = align.align(args.imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    if args.verbose:
        print("  + Face alignment took {} seconds.".format(time.time() - start))

    start = time.time()
    rep = net.forward(alignedFace)
    if args.verbose:
        print("  + OpenFace forward pass took {} seconds.".format(time.time() - start))
        print("Representation:")
        print(rep)
        print("-----\n")
    return rep