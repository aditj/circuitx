import cv2
import numpy as np
import imutils
img=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/test_circuit_2.jpg')
red=  [np.array([0,50,50] ),np.array([10,255,255])]
green=[np.array([ 46,235,14]),np.array([ 66,255,264])]
blue=[np.array([100,234,173]),np.array([120,254,253])]
yellow=[np.array([ 18,245,213]),np.array([ 38,265,293])]
colors= [red,green,blue,yellow]
numbers=[0,0,0,0]
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# code to detect no of colors
kernel = np.ones((2,2), np.uint8)

for i in range(4):
    lower,upper = colors[i]

    img=cv2.dilate(img, kernel, iterations=1)
    mask=cv2.inRange(img,lower,upper)
    #cv2.imshow(str(i),mask)

    cnts,_ =  cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if 144>cv2.contourArea(cnt)>10:
            numbers[i]+=1

print(numbers)
cv2.waitKey(0)
cv2.destroyAllWindows()
