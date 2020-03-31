import numpy as np
import cv2

#the below code is used to print all the events present in the opencv lib.

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def clicking_events(event, x, y, flags, parameters):





    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)

        cv2.imshow("image",img)

#here you can use any imgage just unhash any and hast the other one

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("lena.jpg")

cv2.imshow("image",img)

points=[]

#this call backs the clicking_event and passing the value
#in the above defined func
cv2.setMouseCallback("image",clicking_events)

cv2.waitKey(0)
cv2.destroyAllWindows()