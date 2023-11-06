import cv2
import numpy as np
import requests

url = '/abrir/'

print("Reconhecimento facial rodando")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

face_cascade_Path = "haarcascade_frontalface_default.xml"


faceCascade = cv2.CascadeClassifier(face_cascade_Path)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
# names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
names = [None] # add a name into this list
#Video Capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
# Min Height and Width for the  window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        if (confidence < 100):
                id = names[id]
                confidencepercent = "  {0}%".format(round(100 - confidence))
                if (confidence >= 90) and (id is not None):
                    requests.post(url)
        else:
            # Unknown Face
            id = "Who are you ?"
            confidencepercent = "  {0}%".format(round(100 - confidence))
            ret, img = cam.read()
            if (confidence > 50):
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.imwrite("./static/Images/Desconhecido" + ".jpg",  img)

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidencepercent), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)
    # Escape to exit the webcam / program
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
print("\n [INFO] Exiting Program.")
cam.release()
cv2.destroyAllWindows()
