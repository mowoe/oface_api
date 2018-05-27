import requests
import json
import cv2
import urllib

endpoint = "http://localhost:5000/detect?url="
url = "https://how-old.net/Images/faces2/main001.jpg"
resp = requests.get(endpoint+url).text

faces = json.loads(resp)["detected"]

urllib.urlretrieve(url,"/tmp/img.jpg")

img=cv2.imread("/tmp/img.jpg")
for face in faces:
    b,r,l,t = faces[face]
    cv2.rectangle(img,(l,t),(r,b),(255,0,0))
cv2.imshow("lol",img)
cv2.waitKey(0)