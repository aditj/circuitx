import numpy as np
import cv2
import imutils
def length(l):
    p1x,p1y,p2x,p2y=l[0]
    return ((p1x-p2x)**2+(p1y-p2y)**2)**0.5
def unique(p1,p2):
    if length([[p1[0],p1[1],p2[0],p2[1]]])<10:
        return False
    else:
        return True
def ingate(gate,pt):
    mid=[[(gate[0][0]+gate[1][0])/2,(gate[0][1]+gate[1][1])/2,pt[0],pt[1]]]
    if length(mid)<50:
        return True
    else:
        return False

'''
def parallel_lines(l1,l2):
    if min(distance(l1[0],l))

'''
img=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/T4.jpg')
xor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/xor.png')
xnor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/xnor.png')
andi=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/and.png')
nand=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/nand.png')
nor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/nor.png')
or_=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/or.png')
not_=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/not.png')
templates = [xor,xnor,andi,nand,nor,or_,not_]
names=['xor','xnor','and','nand','nor','or','not']
copy=img.copy()
#img = cv2.dilate(img,kernel,iterations = 2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold=[0.9,0.9,0.9,0.95,0.95,0.95,0.9]
gates=[[],[],[],[],[],[],[]]
for i in range(len(templates)):
    template=cv2.cvtColor(templates[i], cv2.COLOR_BGR2GRAY)
    (tH, tW) = template.shape[:2]
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( result >= threshold[i])
    pts=[]
    for pt in zip(*loc[::-1]):
        pts.append([pt,(pt[0] + tW, pt[1] + tH)])
        cv2.rectangle(img, pt, (pt[0] + tW, pt[1] + tH), (255,255,255), -1)

    gates[i]=[names[i],pts]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
gray_copy=gray.copy()
#gray = cv2.erode(gray,kernel,iterations = 2)

edged = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(gray,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contours)
cv2.drawContours(gray_copy, contours, -1, (255, 255, 0), 3)
#cv2.imshow("LS",gray_copy )
height, width = img.shape[:2]
blank = 255 * np.ones(shape=[height,width,  3], dtype=np.uint8)

unique_points=[]

lsd = cv2.createLineSegmentDetector(0)
lines,width,prec,_ = lsd.detect(gray)
drawn=[]
for i in range(len(lines)):
    if length(lines[i])>20:
        drawn_img = lsd.drawSegments(blank,lines[i])
        drawn.append(lines[i])

        flag1=True
        flag2=True

        if len(unique_points)==0:
            unique_points.append([lines[i][0][0],lines[i][0][1]])
            unique_points.append([lines[i][0][2],lines[i][0][3]])
            continue

        if len(unique_points)!=0:
            for j in range(len(unique_points)):
                if unique(unique_points[j],[lines[i][0][0],lines[i][0][1]])==False and unique(unique_points[j],[lines[i][0][2],lines[i][0][3]]):
                    flag1=False
                    flag2=False
                    break
                elif(unique(unique_points[j],[lines[i][0][0],lines[i][0][1]])==False):
                    flag1=False
                    break
                elif (unique(unique_points[j],[lines[i][0][2],lines[i][0][3]])==True):
                    flag2=False
                    break
                else:
                    continue
        if flag1==True  and len(unique_points)!=0:
            unique_points.append([lines[i][0][0],lines[i][0][1]])
            continue
        if flag2==True and len(unique_points)!=0:
            unique_points.append([lines[i][0][2],lines[i][0][3]])
'''
for a in range(len(gates)):
    unique_gates=[]
    indexes=[]
    for i in range(len(gates[a][1])):
        for j in range(i+1,len(gates[a][1])):
            if unique(gates[a][1][i],gates[a][1][j])==False:
                indexes.append(j)
    for i in range(len(gates[a][1])):
        if i not in indexes:
            unique_gates.append([names[a],gates[a][1][i]])
    gates[a]=unique_gates'''
indexes=[]

u=[]
for i in range(len(unique_points)):
    for j in range(i+1,len(unique_points)):
        if unique(unique_points[i],unique_points[j])==False:
            indexes.append(j)
            indexes.append(i)
print(indexes)
indexes.sort()
#u.append(unique_points[0])
u+=unique_points[0:indexes[0]]
for i in range(len(indexes)-1):
    u+=unique_points[indexes[i]+1:indexes[i+1]]
u+=unique_points[indexes[len(indexes)-1]:len(unique_points)]
unique_points=u
print(len(gates[2][1]))
gatepts=[]
for pt in unique_points:
    for i in range(len(gates)):
        for j in range(len(gates[i][1])):
            if ingate(gates[i][1][j],pt):
                gatepts.append([names[i],pt])

print(gatepts)
for i in range(len(unique_points)):
    copy=cv2.circle(copy,(unique_points[i][0],unique_points[i][1]), 10, (255,0,0),1)
for cnt in contours:
    for i in range(len(gatepts)):
        for j in range(i+1,len(gatepts)):
            if (cv2.pointPolygonTest(cnt, tuple(gatepts[i][1]), True)>=0) and (cv2.pointPolygonTest(cnt, tuple(gatepts[j][1]), True)>=0) :
                print(gatepts[i],gatepts[j])
#drawn_img = lsd.drawSegments(blank,drawn)
cv2.imshow("LSD",copy )


cv2.waitKey(1000000)
cv2.destroyAllWindows()
