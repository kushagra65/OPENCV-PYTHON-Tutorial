import cv2
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1080)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
while(cap.isOpened()):
    ret,frame=cap.read()#read will return true if the frame is available
                        #and will be saved in the frame & ret will be TRUE
    if ret==True:
        font=cv2.FONT_ITALIC
        text="width:"+str(cap.get(3))+" height:"+str(cap.get(4))#variable that we want to show
                    #str method to convert integer to string
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)



        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



cap.release()
cv2.destroyAllWindows()