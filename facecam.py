import cv2
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
    for (x,y,w,h) in faces:
      
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
        cv2.imshow("face detection",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
cam.release()
cv2.destroyAllWindows()