import cv2
# video_path=cv2.VideoCapture("/home/user/Downloads/1.mp4")


# while True:
#     sucess , frame=video_path.read()
    
#     print(sucess)
#     if sucess == False:
#         break
#     cv2.imshow("video display",frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#        break


# camera access
camera_index="-2,-1,0,1,2"
video_path=cv2.VideoCapture(0)


while True:
    sucess , frame=video_path.read()
    print("image_shape: ",frame.shape)
    # # rectangle
    cv2.rectangle(frame,pt1=(115,242),pt2=(415,363),color=(0,255,255),thickness=cv2.FILLED)

    # circle
    cv2.circle(frame,center=(330,298),radius=50,color=(255,0,255),thickness=cv2.FILLED)

    # # text
    cv2.putText(frame,
            text="luminar",
            org=(150,278),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(0,255,0),
            thickness=2)    
    
    print(sucess)
    if sucess == False:
        break
    cv2.imshow("video display",frame)
    if cv2.waitKey(1) & 0xFF == 27:
       break
   
