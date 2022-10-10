import array
from datetime import datetime, time
import os
from operator import index

import cv2
import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file(input("Введите расположение файла>>>"))

face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    img_path = f"{timestr}.jpeg"
    pil_image.save(fp=img_path, format="JPEG")

img = cv2.imread(img_path)
cv2.imshow("img", img)
cv2.waitKey(0)

# for face_landmarks in face_landmarks_list:
#
#     for facial_feature in face_landmarks.keys():
#         d.line(face_landmarks[facial_feature], width=5)
#
# pil_image.show()
