import cv2
cap=cv2.VideoCapture(0 );#we can also pass the dir of the file we need to read
                        #or we need to provide the device index of the web cam
                        #by defauld the index will be 0 or -1

#fourcc  is the codec of the file which we are gonna save
#you can visit the the www.fourcc.org/codecs.php
#to know more about the codec

fourcc=cv2.VideoWriter_fourcc(*'XVID')

#this code can also be given as
#fourcc=cv2.VideoWriter_fourcc('X','V','I','D')

out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#we can pass True in while loop also

#but the cap.Opened we have passed in the below line
#gives 2 arguments if the the video is captured then it Returns = True
#else it returns False


while(cap.isOpened):
    ret,frame=cap.read()#read will return true if the frame is available
                        #and will be saved in the frame & ret will be TRUE

    #now we will use a methord which will allow us to convert a color
    #image in a Gray Scale image

    #as ret is a boolean value we will first check if is it true or false

    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        out.write(frame)#capturing the image

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#frame is passed to the cvt where the
                                                #image RGB frames are converted the
                                                #Grayscale frame

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    else:
        break
    #This statement will work such a way the
    #we will not be able to close the window even if we try
    #the last option to close the window is to press the "q" to close


#after capturing the video it is important to release the resoureces
cap.release()
out.release
cv2.destroyAllWindows()
