import numpy as np
import cv2

#the below code is used to print all the events present in the opencv lib.

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def clicking_events(event, x, y, flags, parameters):

    #event created for printing the color of the image

    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green = img[y, x, 0]
        red = img[y, x, 0]
        bgr=str(blue)+","+str(green)+","+str(red)
        font = cv2.FONT_ITALIC
        cv2.putText(img, bgr, (x, y), font, 1, (255, 255, 255), 2)
        cv2.imshow("image",img)

    #event for printing the position of the mouse on the image

    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        font=cv2.FONT_ITALIC
        strXY=str(x)+" "+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(0,255,255),2)
        cv2.imshow("image",img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("lena.jpg")

cv2.imshow("image",img)

#this call backs the clicking_event and passing the value 
#in the above defined func
cv2.setMouseCallback("image",clicking_events)

cv2.waitKey(0)
cv2.destroyAllWindows()