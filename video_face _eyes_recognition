import cv2
video_path=cv2.VideoCapture("/home/user/Downloads/1.mp4")
face_cascade=cv2.CascadeClassifier("/home/user/Deep_Learning1/face_detection/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("/home/user/Deep_Learning1/face_detection/haarcascade_eye.xml")
# img_grey=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)



while True:
    sucess , frame=video_path.read()
    faces=face_cascade.detectMultiScale(frame)
    eyes=eye_cascade.detectMultiScale(frame)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,255),thickness=3)
    # x1=(x,y) x2=(x+w,y+h)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,255),thickness=3)
        print(sucess)
    if sucess == False:
        break
    cv2.imshow("video display",frame)
    if cv2.waitKey(1) & 0xFF == 27:
       break
