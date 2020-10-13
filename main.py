import cv2
import numpy as np
import imutils

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

cam_num = -1
cap = cv2.VideoCapture(cam_num)


def main():
	if not (cap.isOpened()):
		print("cant open camera")
		return
	while True:

		ret, frame = cap.read()
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			# Create rectangle aroun#d the face
			cv2.rectangle(image, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 25, 25), 1)
		cv2.imshow("img", image)
		k = cv2.waitKey(30)
		if k == 27:
			break

if __name__ == "__main__":
	main()