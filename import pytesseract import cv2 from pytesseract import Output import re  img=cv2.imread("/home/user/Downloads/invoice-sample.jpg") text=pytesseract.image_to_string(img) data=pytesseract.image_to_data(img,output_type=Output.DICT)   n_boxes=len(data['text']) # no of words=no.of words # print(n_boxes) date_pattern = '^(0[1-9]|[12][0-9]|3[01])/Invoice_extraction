import pytesseract
import cv2
from pytesseract import Output
import re

img=cv2.imread("/home/user/Downloads/invoice-sample.jpg")
text=pytesseract.image_to_string(img)
data=pytesseract.image_to_data(img,output_type=Output.DICT)


n_boxes=len(data['text'])
# no of words=no.of words
# print(n_boxes)
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
mail_pattern =	'^[a-z0-9](\.?[a-z0-9]){5,}@example\.net$'


# question: detect date using regular expression
    

for i in range(n_boxes):
    if data['conf'][i]>70:
        if re.match(date_pattern,data['text'][i]) or re.match(mail_pattern,data['text'][i]): 
            x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)

   
cv2.imshow("img1",img)
cv2.waitKey()
cv2.destroyAllWindows()
