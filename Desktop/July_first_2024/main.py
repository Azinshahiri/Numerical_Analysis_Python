import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
pic= Image.open("/Users/azinshahiri/Desktop/Computer_V/CV_MY_1/DATA/00-puppy.jpg")
# Image.show(pic)
blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)
#print(cv2.rectangle(blank_img,pt1=(384,0),pt2=(510,150), color=(0,255,0), thickness=3))
#print(cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300), color=(0,0,255), thickness=3))
#print(cv2.circle(blank_img,center=(300,300),radius=200, color=(255,0,0), thickness=3))
#cv2.line(blank_img,pt1=(0,0),pt2=(512,512), color=(0,255,0), thickness=3)
#font=cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(blank_img,text="Hello", org=(10,500),fontFace=font, fontScale=4,color=(255,255,255),thickness=3,
#            lineType=cv2.LINE_AA)
vertics=np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)
pts= vertics.reshape((-1,1,2))
cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=10)
plt.imshow(blank_img)
plt.show()







