import numpy as np
import cv2

img=cv2.imread('lena.jpg',1)

#TO draw on a image created by numpy library
#remove the # from the below line

#img=np.zeros([600,600,3],np.uint8)




                                    #ble,green,red ,
                                    # ypu can get color combination
                                    #in the rgb color picker
#method to print a line

#thich cv2.line takes 4 arguments 1- image,2- co-ordinates,color,thickness


img=cv2.line(img,(0,0),(255,255), (255,255,), 5)#color is picked in a BGR format

# method to print an arrow

img=cv2.arrowedLine(img,(0,90),(300,350), (255,255,255), 5)

# method to print a rectangle

# rectangle has 4 arguments 1-image,2- point-1,3-point-2,thichkness,linetype,shift

img=cv2.rectangle(img,(384,0),(510,190),(0,0,232),10)#passing the value -ve value in the
                                                    #place of the thickness them it will fill
                                                    #the rectangle with the provided color

#method to draw a circle

#circle has args img,center,radius,color,thickness

img=cv2.circle(img,(44,63),63,(0,255,0),-1)

#method to put text on an image

#arguments img,text,org,fontFace
font=cv2.FONT_ITALIC

imf=cv2.putText(img,"beauty",(10,500),font,4,(0,0,0),10)

#there are many other diffirent methods do try those ones


cv2.imshow('image',img)

# unhash the below code to save the file

#cv2.imwrite ('lena_fun.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()