import cv2
img=cv2.imread("/home/user/Desktop/1.jpg")
face_cascade=cv2.CascadeClassifier("/home/user/Deep_Learning1/face_detection/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("/home/user/Deep_Learning1/face_detection/haarcascade_eye.xml")
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(img_grey)
# eyes=eye_cascade.detectMultiScale(img_grey)
# grey_scale image is preferred because only a single value has  to be processed otherwise 3 values need to be processed
print(faces)
# print(eyes)
# # rectangle
# cv2.rectangle(img,pt1=(422,85),pt2=(446,109),color=(0,255,255),thickness=cv2.FILLED)
# cv2.rectangle(img,pt1=(454,88),pt2=(475,109),color=(0,255,255),thickness=cv2.FILLED)
# cv2.rectangle(img,pt1=(422,85),pt2=(446,109),color=(0,255,255),thickness=cv2.FILLED)
# cv2.rectangle(img,pt1=(134,198),pt2=(155,219),color=(0,255,255),thickness=cv2.FILLED)
# cv2.rectangle(img,pt1=(238,79),pt2=(260,101),color=(0,255,255),thickness=cv2.FILLED)
# cv2.rectangle(img,pt1=(339,38),pt2=(364,63),color=(0,255,255),thickness=cv2.FILLED)

for (x,y,w,h) in faces:
     cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,255),thickness=3)
# x1=(x,y) x2=(x+w,y+h)

# for (x,y,w,h) in eyes:
#     cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,255),thickness=3)

# # x,y,w,h values
cv2.imshow("img1",img)
cv2.waitKey()
cv2.destroyAllWindows()
# faces
# [[422  85  24  24]
#  [454  88  21  21]
#  [210  67  25  25]
#  [134 198  21  21]
#  [238  79  22  22]
#  [339  38  25  25]
#  [455 266  22  22]
#  [446  82  28  28]
#  [195 271  22  22]
#  [390 280  28  28]
#  [238 234  27  27]
#  [173 302  48  48]]
