#this program takes a inpur from the user if we want to save a image
# s input is taken as a yes to save a copy of lena
# or if we press any other button than s then the image will not be saved


import cv2
img=cv2.imread('lena.jpg',-1)
#arguments on cv2.imread()---
# seacond argument specifies the way image should be read.
# 1-loads a color image
# 0- loads a grayscale image
# -1 - loads image as such including alpha channel
cv2.imshow('image',img)

k=cv2.waitKey(0) & 0xFF #& 0xFF  is a mask if using a 64 os this is recommended
#wait key is a binding key 5000 is the mili seacond as 5 sec
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):

#it destroys all the windows

    cv2.imwrite ('lena_copy.png',img)

#creates a new imag
#here we just copied the previous one
