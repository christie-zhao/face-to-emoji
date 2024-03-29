from PIL import Image, ImageDraw, ImageFilter
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2


emotion_dict= {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}


size = 10


# Load the jpg file into a numpy array
image = face_recognition.load_image_file("test_images/rajeev.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.\n\n".format(len(face_locations)))

for face_location in face_locations:
    
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}\n\n".format(top, left, bottom, right))
    
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    size = bottom - top



face_image = cv2.resize(image, (48,48))
face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
model = load_model("./emotion_detector_models/model_v6_23.hdf5")


predicted_class = np.argmax(model.predict(face_image))
print(predicted_class)
label_map = dict((v,k) for k,v in emotion_dict.items())
predicted_label = label_map[predicted_class]
print(predicted_label)
print


# TODO: open correct Joseph image
im1 = Image.open('./graphics/anger.png')

copyIm = Image.open('test_images/rajeev.jpg').copy()

fml = im1.resize((size, size))

copyIm.paste(fml, (0,0), fml)
copyIm.save('test_images/rajeevjoseph.jpg')
copyIm.show()
