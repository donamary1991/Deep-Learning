# import cv2

# # print("hello")
# img=cv2.imread("/home/user/Desktop/images.jpeg")


# print(img)
# cv2.imshow("image",img)
# cv2.waitKey(6000)
# # in msec
# cv2.destroyAllWindows()
# # esc key for closing


# 30/12/2024


# import cv2

# # print("hello")
# img=cv2.imread("/home/user/Desktop/images.jpeg")

# # shape of image
# print("image_shape: ",img.shape)
# # (height,width,shape)

# # convert shape tof image
# converted_img=cv2.resize(img,(300,300))
# cv2.imshow("binary_image",converted_img)

# # greyscale
# img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # print(img)
# # method is used to convert an image from one color space to another. There are more than 150 color-space conversion methods available in OpenCV
# # cv read image in BGR format
# # cv2.imshow("image",img_grey)

# # binary-black+white==convert from greyscale==with the help of theshold(here-120)
# thresh,bin_image=cv2.threshold(img_grey,120,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(thresh)
# # THRESH_OTS-tofind threshold using algorithm

# # save file in jpg format

# # cv2.imwrite("grey_img.jpg",img_grey)
# # cv2.imwrite("bin_image.jpg",bin_image)

# # rectangle
# cv2.rectangle(img,pt1=(300,400),pt2=(200,500),color=(255,0,0),thickness=5)

# # cv2.imshow("binary_image",bin_image)
# # # imshow convert in to RGB form
# cv2.waitKey()
# # in msec
# cv2.destroyAllWindows()
# # esc key for closing

31/12/2024
# import cv2
# img=cv2.imread("/home/user/Desktop/images.jpeg")

# # shape of image
# print("image_shape: ",img.shape)
# # (height,width,shape)

# # circle
# cv2.circle(img,center=(300,300),radius=100,color=(0,255,0),thickness=cv2.FILLED)

# # text
# cv2.putText(img,
#             text="Hello...",
#             org=(100,250),
#             fontFace=cv2.FONT_HERSHEY_COMPLEX,
#             fontScale=1,
#             color=(0,255,0),
#             thickness=2)
# # RGB
# cv2.imshow("image",img)
# cv2.waitKey()
# cv2.destroyAllWindows



# assignment
import cv2
img=cv2.imread("/home/user/Desktop/1.jpg")

# shape of image
print("image_shape: ",img.shape)
# (height,width,shape)

# # rectangle
cv2.rectangle(img,pt1=(127,253),pt2=(415,363),color=(0,255,255),thickness=cv2.FILLED)

# circle
cv2.circle(img,center=(300,300),radius=50,color=(255,0,255),thickness=cv2.FILLED)

# # text
cv2.putText(img,
            text="luminar",
            org=(150,278),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(0,255,0),
            thickness=2)
# RGB
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows


