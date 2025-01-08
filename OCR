# tesseract--google frame work for OCR
# easyOCR-->frame work for OCR
# Detecting Text from picture==OCR
import pytesseract
import cv2
from pytesseract import Output

img=cv2.imread("/home/user/Desktop/IvV2y.png")

text=pytesseract.image_to_string(img)
data=pytesseract.image_to_data(img,output_type=Output.DICT)
print(text)
print(data)
print(data.keys())
# # print("text..>>",data['text'])
# # print("confidence--->",data['conf'])
# for i in data:
#     print(f'{i} ---->{data[i]}')


# text="" <=> confidence=-1


n_boxes=len(data['text'])
# no of words=no.of words
print(n_boxes)


for i in range(n_boxes):
    x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)
    # but these boxes confined in words as well as in all single lines and in whole sentence.
    

for i in range(n_boxes):
    if data['conf'][i]>70:
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)



    
cv2.imshow("img1",img)
cv2.waitKey()
cv2.destroyAllWindows()
