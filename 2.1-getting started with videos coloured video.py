import cv2
cap=cv2.VideoCapture(0);#we can also pass the dir of the file we need to read
                        #or we need to provide the device index of the web cam
                        #by defauld the index will be 0 or -1
while(True):
    ret,frame=cap.read()#read will return true if the frame is available
                        #and will be saved in the frame & ret will be TRUE
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    #This statement will work such a way the
    #we will not be able to close the window even if we try
    #the last option to close the window is to press the "q" to close


#after capturing the video it is important to release the resoureces
cap.release()
cv2.destroyAllWindows()
