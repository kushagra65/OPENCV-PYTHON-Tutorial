import cv2
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1080)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
while(True):
    ret,frame=cap.read()#read will return true if the frame is available
                        #and will be saved in the frame & ret will be TRUE

    #now we will use a methord which will allow us to convert a color
    #image in a Gray Scale image

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#frame is passed to the cvt where the
                                                #image RGB frames are converted the
                                                #Grayscale frame

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()