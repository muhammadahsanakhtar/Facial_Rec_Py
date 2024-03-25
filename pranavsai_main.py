#Pranav Sai

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from keras.models import load_model
import numpy as np
from alexa import alexa

facedetect = cv2.CascadeClassifier('har.xml')

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
font=cv2.FONT_HERSHEY_COMPLEX


model = load_model('keras_model.h5')


def get_className(classNo):
	if classNo==0:
		return "Pranav Sai"
	elif classNo==1:
			return "The Best Dad Ever!"


while True:
	sucess, imgOrignal=cap.read()
	faces = facedetect.detectMultiScale(imgOrignal,1.3,5)
	for x,y,w,h in faces:
		crop_img=imgOrignal[y:y+h,x:x+h]
		img=cv2.resize(crop_img, (224,224))
		img=img.reshape(1, 224, 224, 3)
		prediction=model.predict(img)
		classIndex = np.argmax(prediction,axis=-1)
		probabilityValue=np.amax(prediction)

		cv2.rectangle(imgOrignal,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.rectangle(imgOrignal, (x,y-40),(x+w, y), (0,255,0),-2)
		cv2.putText(imgOrignal, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)

		cv2.imshow("Pranav's Facial Recognition Model",imgOrignal)
		k=cv2.waitKey(1)
		if k==ord('q'):
			cap.release()
			cv2.destroyAllWindows()
























